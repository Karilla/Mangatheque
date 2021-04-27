from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(150))
    pseudo = db.Column(db.String(150))
    manga = db.relationship('Manga')

class Manga(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    mangaName = db.Column(db.String(150),unique=True) 
    author = db.Column(db.String(150))
    tome = db.relationship('Tome')
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

class Tome(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(150))
    numberOfTome = (db.Integer)
    manga_id = db.Column(db.Integer,db.ForeignKey('manga.id'))