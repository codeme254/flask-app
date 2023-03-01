from z_market_package import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user
from z_market_package.models import Product
from z_market_package.models import Buyer
from z_market_package.models import Seller
from z_market_package.models import User
from z_market_package.forms import RegisterUserForm, LoginForm
from z_market_package import db

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

@app.route("/user-registration", methods = ['GET', 'POST'])
def register_user():
    user_registration_form = RegisterUserForm()
    if user_registration_form.validate_on_submit():
        new_user = User(
            first_name = user_registration_form.first_name.data,
            last_name = user_registration_form.last_name.data,
            email_address = user_registration_form.email_address.data,
            prefered_username = user_registration_form.username.data,
            hashed_password = user_registration_form.password.data,
            confirm_password_hash = user_registration_form.confirm_password.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('all_products'))
    if user_registration_form.errors != {}:
        for error_message in user_registration_form.errors.values():
            flash("There was an error: {}".format(error_message))
    return render_template("user-registration.html", user_registration_form=user_registration_form)

@app.route("/login", methods = ['GET', 'POST'])
def login_a_user():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # check if the user exists
        attempted_user = User.query.filter_by(prefered_username=login_form.username.data).first()
        # if attempted user exists, check if password matches
        # we need to unhash the password
        if attempted_user and attempted_user.check_password_correction(attempted_password=login_form.password.data):
            login_user(attempted_user)
            flash("Success! You are logged in as {}".format(attempted_user.prefered_username), category="success")
            return redirect(url_for('all_products'))
        else:
            flash("Username and password do not match, please try again.", category="danger")
    return render_template("login.html", login_form=login_form)
