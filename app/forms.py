import phonenumbers
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, InputRequired, Length,
                                NumberRange, ValidationError)

from app.models import City, Registration


class ConsultationForm(FlaskForm):
    lastname = StringField('Vezetéknév', validators=[DataRequired(), Length(min=1, max=64)])
    firstname = StringField('Keresztnév', validators=[DataRequired(), Length(min=1, max=64)])
    age = IntegerField('Életkor', validators=[NumberRange(min=0, max=120), InputRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Length(min=5, max=320), Email()])
    postcode = IntegerField('Irányítószám', validators=[InputRequired(), NumberRange(min=0, max=9999)])
    city = StringField('Település', validators=[DataRequired(), Length(min=1, max=128)])
    address = StringField('Cím', validators=[DataRequired(), Length(min=1, max=256)])
    phone = StringField('Telefonszám', validators=[DataRequired()])
    ssn = StringField('TAJ-szám', validators=[InputRequired(), Length(min=9, max=9)])

    submit = SubmitField('Elküldés')

    def validate_age(self, age):
        if age.data < 18:
            raise ValidationError('Csak 18 éven felüliek vehetnek részt.')

    def validate_email(self, email):
        if Registration.query.filter_by(email=email.data).first() is not None:
            raise ValidationError('Ezzel az e-mail címmel már regisztráltak.')

    def validate_city(self, city):
        if City.query.filter_by(name=city.data).first() is None:
            raise ValidationError('Hibás településnév')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except:
            raise ValidationError('Hibás telefonszám')
        if Registration.query.filter_by(phone=phone.data).first() is not None:
            raise ValidationError('Ezzel a telefonszámmal már regisztráltak.')

    def validate_ssn(self, ssn):
        if not ssn.data.isnumeric():
            raise ValidationError('Hibás TAJ-szám')
        if Registration.query.filter_by(ssn=ssn.data).first() is not None:
            raise ValidationError('Ezzel a TAJ-számmal már regisztráltak.')
