from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_my_password(self, password):
        self.password = generate_password_hash(password)

    def check_my_password(self, password):
        return check_password_hash(self.password, password)

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String(50), unique=False)
    type = db.Column(db.String(50), nullable=False)
    abilities = db.Column(db.String(250), unique=False)
    classification = db.Column(db.String(250), unique=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.Column(db.String(50), unique=True)
    why = db.Column(db.String(1000), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('post', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)