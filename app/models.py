from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String

from sqlalchemy.dialects.postgresql import UUID
import uuid

from passlib.apps import custom_app_context as pwd_context

from flask import Flask, jsonify

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from app import config

class Users(db.Model):
    __tablename__ = 'Users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(), unique=False)
    email = Column(String(120), unique=False)
    password_hash = Column(db.String())

    def __init__(self, id=None, name=None, email=None, password_hash=None):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        #encrypt(raw_password, method=..., salt_length=...)
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': str(self.id)})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = Users.query.get(data['id'])
        #print(user.name)
        #userId = user.id
        return data['id']


    def __repr__(self):
        return jsonify({'id': self.id, 'name': self.name, 'email': self.email, 'password_hash': self.password_hash})
        #return 'id: %s  name: %s email: %s password_hash: %s' % (self.id, self.name, self.email, self.password_hash)
