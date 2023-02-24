from z_market_package import app
from flask import render_template
from z_market_package.models import Product
from z_market_package.models import Buyer
from z_market_package.models import Seller
from z_market_package.forms import RegisterUserForm

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

@app.route("/user-registration")
def register_user():
    user_registration_form = RegisterUserForm()
    return render_template("user-registration.html", user_registration_form=user_registration_form)
