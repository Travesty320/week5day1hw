from re import S
from tokenize import String
from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon',validators=[DataRequired()])
    submit = SubmitField()

class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()