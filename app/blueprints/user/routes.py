from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import Post
from app import db
from flask_login import current_user, login_required

@app.route('/posts')
@login_required
def posts():
    all_posts = Post.query.all()
    return render_template('profile.html', posts=all_posts)

@app.route('/post/<id>')
@login_required
def post_by_id(id):
    post = Post.query.get(int(id))
    return render_template('single_pokemon.html', post=post)

@app.route('/create-post', methods=["POST"])
@login_required
def create_post():
    pokemon = request.form['inputPokemonBuddy']
    why = request.form['inputTeamName']
    new_post = Post(pokemon=pokemon,why=why)
    db.session.add(new_post)
    db.session.commit()
    flash('Post created successfully', 'success')
    return redirect(url_for('user.posts'))
