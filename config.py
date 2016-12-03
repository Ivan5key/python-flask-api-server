import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/flask'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


DEBUG = False
TESTING = False
CSRF_ENABLED = True
#SECRET_KEY = 'this-really-needs-to-be-changed'
SECRET_KEY = '266701638:AAGVzskjP83y2Hk4gfI74v9ceUH_gVfpr1k'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/DDS_database'
DEBUG = False
DEVELOPMENT = True
DEBUG = True
DEVELOPMENT = True
DEBUG = True
TESTING = True
