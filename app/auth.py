from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__)


@auth.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Successfully logged', category='success')
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Email does not exist', category='error')            

    return render_template("login.html")

@auth.route('/sign-up',methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('Email already exist',category='error')
        elif len(name) > 12 or len(name) < 2:
            flash('Name lenght must be greater than 2 and lesser than 12',category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4',category='error')
        elif password != password2:
            flash('Password must be the same',category='error')
        elif len(password) < 7:
             flash('Password must be greater than 7',category='error')
        else:
            new_user = User(email=email,pseudo=name,password=generate_password_hash(password,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created',category='success')

    return render_template("signup.html")