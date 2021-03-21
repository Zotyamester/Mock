from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    registrations = db.relationship('Registration', backref='city', lazy='dynamic')
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(64))
    firstname = db.Column(db.String(64))
    age = db.Column(db.Integer)
    email = db.Column(db.String(320), index=True, unique=True)
    postcode = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(14), index=True, unique=True)
    ssn = db.Column(db.String(9), index=True, unique=True)
    answers = db.relationship('Answer', foreign_keys='Answer.rid', backref='registration', lazy='dynamic')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(128))
    answers = db.relationship('Answer', foreign_keys='Answer.qid', backref='question', lazy='dynamic')

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rid = db.Column(db.Integer, db.ForeignKey('registration.id'))
    qid = db.Column(db.Integer, db.ForeignKey('question.id'))
    value = db.Column(db.Boolean)
