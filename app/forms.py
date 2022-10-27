from re import S
from tokenize import String
from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class PokemonForm(FlaskForm):
    pokemon = StringField('Pokemon',validators=[DataRequired()])
    submit = SubmitField()
    
class CatchPokemon(FlaskForm):
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

class CreateRoster(FlaskForm):
    pokemon1 = StringField('Pokemon1', validators=[InputRequired()])
    pokemon2 = StringField('Pokemon2', validators=[InputRequired()])
    pokemon3 = StringField('Pokemon3', validators=[InputRequired()])
    pokemon4 = StringField('Pokemon4', validators=[InputRequired()])
    pokemon5 = StringField('Pokemon5', validators=[InputRequired()])
    pokemon6 = StringField('Pokemon6', validators=[InputRequired()])
    submit = SubmitField()