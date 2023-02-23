from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///z_market.db'

db = SQLAlchemy(app=app)
from z_market_package import routes