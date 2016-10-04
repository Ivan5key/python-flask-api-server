from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Users(db.Model):
    __tablename__ = 'Users'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=False)

    def __init__(self, id=None, name=None, email=None):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User('%s','%s','%s')>" % (self.id, self.name, self.email)
