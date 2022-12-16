from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from .models import Post, Pokemon
from app import db
from flask_login import current_user, login_required

@app.route('/')
def home():
    all_pokemon = Pokemon.query.all()
    return render_template('home.html', pokemons=all_pokemon, user=current_user)

@app.route('/about')
def about():
    return render_template('about.html')