from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from os import getenv

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = mysql+pymysql://root:11@mysql:3306/player_db
app.config['SECRET_KEY'] = 'MYSTIC'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes