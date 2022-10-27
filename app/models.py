from re import U
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin, user_logged_in


db = SQLAlchemy()

pokedex = db.Table('pokedex', 
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')), 
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    caught = db.relationship("Pokemon",
        secondary = pokedex,
        backref = db.backref('trainer', lazy= 'dynamic'),
        lazy = 'dynamic'
    )
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def catch(self, pokemon):
        self.caught.append(pokemon)
        db.session.commit()



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_name = db.Column(db.String)
    base_hp = db.Column(db.Integer)
    base_att = db.Column(db.Integer)
    base_def = db.Column(db.Integer)
    sprite = db.Column(db.String)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, poke_name, base_hp, base_att, base_def, sprite):
        self.poke_name = poke_name
        self.base_hp = base_hp
        self.base_att = base_att
        self.base_def = base_def
        self.sprite = sprite
        

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()
