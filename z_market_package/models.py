from z_market_package import db
from datetime import datetime
class Product(db.Model):
    """
    model for a product in the database
    """
    id = db.Column(db.Integer(), primary_key=True)
    productName = db.Column(db.String(), nullable=False)
    productDescription = db.Column(db.String(), nullable=False)
    buyersWanting = db.Column(db.Integer(), nullable=False)
    sellersSelling = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)

class Buyer(db.Model):
    """
    model for a buyer in the database
    """
    id = db.Column(db.Integer(), primary_key=True)
    buyerName = db.Column(db.String(), nullable=False)
    charisma = db.Column(db.Integer(), nullable=False)
    goodsBought = db.Column(db.Integer(), nullable=False)
    joinedOn = db.Column(db.String(), nullable=False)
    emailAddress = db.Column(db.String(), nullable=False)

class Seller(db.Model):
    """
    model for a seller in the database
    """
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    sellerName = db.Column(db.String(), nullable=False)
    goodsSold = db.Column(db.Integer(), nullable=False)
    charisma = db.Column(db.Integer(), nullable=False)
    emailAddress = db.Column(db.String(), nullable=False)