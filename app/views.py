from app import app
from flask import Flask, jsonify, make_response, abort, request
from app import db
from models import Users

import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('postgresql://postgres:root@localhost:5432/flask', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

@app.route('/')
def index():
    return str(uuid.uuid4())

#create
@app.route('/users', methods=['POST'])
def get_tasks():
    #user = Users(str(uuid.uuid4()), name, email)

    #db_session.add(user)/name=<string:name>email=<string:email>'
    #db_session.commit()
    if not request.json or not 'name' in request.json:
        abort(400)
    if not request.json or not 'email' in request.json:
        abort(400)

    user = Users(str(uuid.uuid4()), request.json['name'], request.json['email'])
    db_session.add(user)
    db_session.commit()

    #ourUser = db_session.query(Users).filter_by(name = 'postwtrtgre1213s').first()
    #ourUser = Users.query.filter(Users.name == 'postwtrtgre1213s').first()
    #return ourUser[1]

    #return jsonify({'tasks': 'complete!'})
    #return name
    return jsonify({'name': request.json['name'], 'email': request.json['email']})

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
