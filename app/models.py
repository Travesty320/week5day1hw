from re import U
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id')) 
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()



class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, id, pokemon_id, user_id):
        self.id = id
        self.pokemon_id = pokemon_id
        self.user_id = user_id



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, id, team_id, user_id):
        self.id = id
        self.team_id = team_id
        self.user_id = user_id
