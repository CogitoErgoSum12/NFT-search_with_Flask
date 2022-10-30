from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from packets import models, routes
import psycopg2


app = Flask(__name__)
app.secret_key = '!@#$%^&*'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/python'
app.config['SQLALCHEMY TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

manager = LoginManager(app)
manager.login_view = 'login_page'

with app.app_context():
    db.create_all()


