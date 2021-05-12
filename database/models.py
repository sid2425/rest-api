from .db import db

class AddressBookHolding(db.Document):
    name = db.StringField(required=True)
    address = db.StringField(required=True)
    city = db.StringField(required=True)
    state=db.StringField(required=True)
    country=db.StringField(required=True)
    pincode=db.IntField(required=True)
    phonenumber=db.IntField(required=True)
    email = db.StringField(required=True)