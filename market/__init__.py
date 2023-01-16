from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///market.db"
app.config['SECRET_KEY']='f98db004489cd35656878e3f'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes