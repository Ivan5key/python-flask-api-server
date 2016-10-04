from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask_uuid import FlaskUUID

app = Flask(__name__)
FlaskUUID(app)

app.config.from_object('config')
db = SQLAlchemy(app)

from models import Users
from app import views, models
