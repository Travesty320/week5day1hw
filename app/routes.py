from flask import render_template, url_for, redirect
from app import app
from app.forms import PokemonForm
from app.pokefinder import *

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
