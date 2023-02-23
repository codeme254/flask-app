from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///z_market.db'

db = SQLAlchemy(app=app)


# Models for now
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
    joinedOn = db.Column(db.String(), default=datetime.date.today(), nullable=False)
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

@app.route("/")
@app.route("/home")
def index_page():
    return render_template("index.html")

@app.route("/all-products")
def all_products():
    all_products = Product.query.all()
    return render_template("all-products.html", all_products=all_products)

@app.route("/all-buyers")
def all_buyers():
    all_buyers = Buyer.query.all()
    return render_template("buyers.html", all_buyers=all_buyers)

@app.route("/all-sellers")
def all_sellers():
    all_sellers = Seller.query.all()
    return render_template("sellers.html", all_sellers=all_sellers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)