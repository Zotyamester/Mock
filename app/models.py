from app import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    registrations = db.relationship('Registration', backref='city', lazy='dynamic')
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    postcode = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    address = db.Column(db.String(256))
    age = db.Column(db.Integer)
    email = db.Column(db.String(320))
    phone = db.Column(db.String(14))
    ssn = db.Column(db.String(9))
