from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///z_market.db'
app.config['SECRET_KEY'] = 'e5d35e6a3648d2b2d54041f6e621f7749f33807463d9306c'

db = SQLAlchemy(app=app)
login_manager = LoginManager(app)

bcrypt = Bcrypt(app=app)
from z_market_package import routes