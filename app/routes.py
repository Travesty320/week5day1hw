import re
from flask import render_template, url_for, redirect, request, flash
from app import app
from app.forms import Login, PokemonForm, SignUp, CreateRoster
from app.pokefinder import *
from app.models import Pokemon, User, db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def realHomePage():
    return render_template('index.html')



@app.route('/signup', methods = ["GET", "POST"])
def signMeUp():
    form = SignUp()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            my_user = User(username, email, password)
            my_user.saveToDB()
            return redirect(url_for('logMeIn'))
            
    return render_template('signup.html', s=form)


@app.route('/login', methods = ["GET", "POST"])
def logMeIn():
    form = Login()
    if request.method == "POST":
        print('post method made')
        if form.validate():
            username = form.username.data
            password = form.password.data
            print(username, password)
            
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('successfully logged in')
                    login_user(user)
                    return redirect(url_for('realHomePage'))
                else:
                    print('incorrect password')

            else:
                print('user does not exist')
    return render_template('login.html', form=form)

@app.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('logMeIn'))


@app.route('/choosepokemon', methods = ['Get', 'Post'])
def checkPokemon():
    form = PokemonForm()
    poke_dict = {}
    if request.method == "POST":
        pname= form.pokemon.data 
        pokemon = PokeFinder(form.pokemon.data)
        poke_q = Pokemon.query.filter(Pokemon.poke_name==pname).first()
        print(poke_q)
        if poke_q:
            pass
        else:
            print(pokemon)
            poke_ql = Pokemon(pokemon['poke_name'],pokemon['base_hp'], pokemon['base_att'], pokemon['base_def'], pokemon['sprite'])
            poke_ql.saveToDB()
        
        return render_template('pokemon.html', form = form, pokemon=pokemon)
    return render_template('pokemon.html', title = 'PokeFinder', form = form, pokemon=poke_dict)

@app.route('/choosepokemon/catch/<id>', methods=["POST"])
@login_required
def catchPokemon(id):
    pokemon = Pokemon.query.get(id)
    current_user.catch(pokemon)
    return redirect('pokemon.html')

@app.route('/team', methods=["GET"])
@login_required
def caughtPokemon():
    pokemon = current_user.caught.all()
    return render_template('team.html', pokemon=pokemon)

@app.route('/choosepokemon')
def pokemon():
    users = User.query.all()
    caught = []
    caught_set = set()
    if current_user.is_authenticated:
        caught = current_user.caughtPokemon.all()
        caught_set = {c.id for c in caught}
    for u in users:
        if u.id in caught_set:
            u.flag=True
    
    
    return render_template('pokemon.html', names=users)



        
