from . import bp as app
from app.blueprints.main.models import User
from app import db, login_manager
from flask import redirect, url_for, render_template, request, flash
from flask_login import login_user, logout_user

@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    password = request.form['password']
    next_url = request.form['next']

    user = User.query.filter_by(email=email).first()
    print(user)
    if user is None:
        flash(f"User with email {email} does not exist.")
    elif user.check_my_password(password):
        print(user)
        login_user(user)
        flash(f"Welcome back {user.trainer_name}", "success")

        if next_url !='':
            return redirect(next_url)
        return redirect(url_for('main.home'))
    else:
        flash('Password incorrect.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')

    email = request.form['email']
    trainer_name = request.form['trainer_name']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    # first_name = request.form['firstName']
    # last_name = request.form['lastName']

    check_user = User.query.filter_by(email=email).first()

    if check_user is not None:
        flash(f"User with email {email} already exists.", 'danger')
    
    elif password != confirm_password:
        flash('Passwords do not match', 'danger')

    else:
        # try:
        new_user = User(email=email, trainer_name=trainer_name, password='')
        new_user.hash_my_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('auth.login'))
        # except:
        #     flash('There was an error.', 'danger')
        return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))