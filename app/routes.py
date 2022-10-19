from flask import render_template
from app import app


@app.route('/')
def realHomePage():
    return render_template('index.html')

@app.route('/favs')
def favsPage():
    favs_list = ['Brand New', 'The Weeknd', 'Kanye West', 'Kid Cudi', 'The Used']
    return render_template('favs.html', names=favs_list)