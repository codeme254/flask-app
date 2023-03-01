from z_market_package import db, login_manager
from datetime import datetime
from z_market_package import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

class User(db.Model, UserMixin):
    """
    Ok, this can just be some normal user who wants to use our app but doesn't
    want to be part of the fahm
    """
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), nullable=False, unique=True)
    prefered_username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    confirm_password = db.Column(db.String(), nullable=False)

    # hashing password logic
    @property
    def hashed_password(self):
        return self.hashed_password
    
    @hashed_password.setter
    def hashed_password(self, plain_text_password):
        self.password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    @property
    def confirm_password_hash(self):
        return self.confirm_password_hash
    
    @confirm_password_hash.setter
    def confirm_password_hash(self, plain_text_passwd):
        self.confirm_password = bcrypt.generate_password_hash(plain_text_passwd).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)