#!/usr/bin/python
import os, subprocess, sys
subprocess.call(['python', 'virtualenv.py', 'flask'])
if sys.platform == 'win32':
    bin = 'Scripts'
else:
    bin = 'bin'
subprocess.call(['python', '-m', 'venv', 'flask'])
#subprocess.call(['easy_install', 'virtualenv'])
subprocess.call([os.path.join('flask', bin, 'easy_install'), 'virtualenv'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'virtualenv'])
subprocess.call([os.path.join('flask', bin, 'virtualenv'), 'flask'])
#subprocess.call(['pip', 'install', 'virtualenv'])
#subprocess.call(['virtualenv', 'flask'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask<0.10.1'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-login'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-openid'])
if sys.platform == 'win32':
    subprocess.call([os.path.join('flask', bin, 'pip'), 'install', '--no-deps', 'lamson', 'chardet', 'flask-mail'])
else:
    subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-mail'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'sqlalchemy==1.0.12'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-sqlalchemy>=2.1'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'psycopg2==2.6.1'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-migrate==1.8.0'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'sqlalchemy-migrate'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-whooshalchemy'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'Flask-UUID'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-wtf'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flask-babel'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'flup'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'Flask-Passlib'])
subprocess.call([os.path.join('flask', bin, 'pip'), 'install', 'Flask-HTTPAuth'])
