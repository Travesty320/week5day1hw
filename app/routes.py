from flask import render_template, url_for, redirect, request
from app import app
from app.forms import Login, PokemonForm, SignUp
from app.pokefinder import *
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user

@app.route('/')
def realHomePage():
    return render_template('index.html')

@app.route('/choosepokemon', methods = ['Get', 'Post'])
def Pokemon():
    form = PokemonForm()
    print(form)
    if form.validate_on_submit():
        pokemon = PokeFinder(form.pokemon.data)
        if isinstance(pokemon, str):
            return 'This is not a valid Pokemon'          
        else:
            return render_template('pokemon.html', pokemon = pokemon, form = form)
    # elif not pokemon:
    #         redirect(url_for('PokeFinder'))
    return render_template('pokemon.html', title = 'PokeFinder', form = form)

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
                    print('succesfully logged in')
                    login_user(user)
                    return redirect(url_for('homePage'))
                else:
                    print('incorrect password')

            else:
                print('user does not exist')
    return render_template('login.html', form=form)

@app.route('/logout')
def logMeOut():
    logout_user()
    return redirect(url_for('logMeIn'))