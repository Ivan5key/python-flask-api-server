from app import app
from flask import Flask, jsonify, make_response, abort, request
from app import db
from models import Users
import json
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:root@localhost:5432/DDS_database', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

from app import auth

import base64

def token_verify(token):
    token = Users.verify_auth_token(token)
    return

@app.route('/')
def index():
    return str(uuid.uuid4())

#auth
@app.route('/login', methods=['GET'])
def user_auth():
    auth = request.headers['Authorization']
    auth = auth.replace('Basic ','')
    username,password = base64.decodestring(auth).split(':')
    user = Users.query.filter(Users.name == username).first()
    if not user or not user.verify_password(password):
        return jsonify({'error': 'Unauthorized', 'status': 401})
    else:
        token = user.generate_auth_token()
        #token = user.verify_auth_token('eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ3NjA0Nzc2MCwiaWF0IjoxNDc2MDQ3MTYwfQ.eyJpZCI6ImFmNDM5OGZiLWMyNjAtNDRmOC1iOTljLTU1MDI5NTgxYzIwNyJ9.-avv5BQ7yRiQK2TtvtJzcZSHqt3XvB61ErxTn1lqfJM')

        return jsonify({'status': 200, 'token': token})

#create user
@app.route('/users', methods=['POST'])
def new_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    elif request.json['name'] == "":
        return jsonify({'error': "'name' is not filled", 'status': 403})
    elif len(request.json['name']) <= 5:
        return jsonify({'error': "'name' must include 4 characters", 'status': 403})
    if not request.json or not 'password' in request.json:
        abort(400)
    elif request.json['password'] == "":
        return jsonify({'error':"'password' is not filled", 'status': 403})
    elif len(request.json['password']) <= 6:
        return jsonify({'error': "'password' must include 6 characters", 'status': 403})

    if not request.json or not 'email' in request.json:
        abort(400)
    elif request.json['email'] == "":
        return jsonify({'error':"'email' is not filled", 'status': 403})

    existingEmail = Users.query.filter(Users.email == request.json['email']).first()
    existingLogin = Users.query.filter(Users.name == request.json['name']).first()
    if existingEmail is None and existingLogin is None:
        password = request.json['password']
        user = Users(str(uuid.uuid4()), request.json['name'], request.json['email'])
        user.hash_password(password)
        db_session.add(user)
        db_session.commit()
        return jsonify({'name': request.json['name'], 'email': request.json['email'], 'status': 201})
    else:
        notAvailableEmail = json.dumps(existingEmail.email)
        print('error')
        return jsonify({'error':'This email is not available', 'email': notAvailableEmail, 'status': 403})

#get item
@app.route('/users/<int:user_id>', methods=['GET'])
def get_task(task_id):
    #users - db
    user = filter(lambda t: t['id'] == user_id, users)
    if len(user) == 0:
        abort(404)
    return jsonify({'task': user[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('WWW-Authenticate', 'Basic realm="Login required"')
  response.headers.add('Access-Control-Allow-Headers', 'Authorization, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  response.headers.add("Access-Control-Allow-Credentials", "true")
  return response
