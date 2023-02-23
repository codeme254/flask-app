#!/usr/bin/env python3

all_sellers = [
        {
            "sellerName": "kimani ngunjiri",
            "goodsSold": 500,
            "charisma": 800,
            "emailAddress": "kimani@gmail.com"
        },
        {
            "sellerName": "elvis rotich",
            "goodsSold": 900,
            "charisma": 1800,
            "emailAddress": "rotich@yahoo.com"
        },
        {
            "sellerName": "cynthia murimi",
            "goodsSold": 700,
            "charisma": 550,
            "emailAddress": "murimi@outlook.com"
        },
        {
            "sellerName": "ken waithaka",
            "goodsSold": 5500,
            "charisma": 9000,
            "emailAddress": "kenwa@gmail.com"
        },
        {
            "sellerName": "naomi bosibori",
            "goodsSold": 1200,
            "charisma": 1700,
            "emailAddress": "naomi@gserve.com"
        },
        {
            "sellerName": "johnstone king",
            "goodsSold": 600,
            "charisma": 560,
            "emailAddress": "kingjohn@gmail.com"
        },
    ]

from main import db, app, Seller

with app.app_context():
    db.create_all()

for seller in all_sellers:
    current_seller = Seller(sellerName=seller['sellerName'], goodsSold=seller['goodsSold'], charisma=seller['charisma'], emailAddress=seller['emailAddress'])
    with app.app_context():
        db.session.add(current_seller)
        db.session.commit()

# sellerName = db.Column(db.String(), nullable=False)
#     goodsSold = db.Column(db.Integer(), nullable=False)
#     charisma = db.Column(db.Integer(), nullable=False)
#     emailAddress = db.Column(db.String(), nullable=False)