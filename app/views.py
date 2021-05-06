from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

from .models import Manga

views = Blueprint('views',__name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        manga_name = request.form.get('mangaName')
        mangaAuthor = request.form.get('mangaAuthor')

        if len(manga_name) > 20:
            flash('Manga name too long (max 20 characters',category='error')
        elif len(mangaAuthor) > 25:
            flash('Manga author name too long (max 25 characters',category='error')
        else:
            new_manga = Manga(manga_name=manga_name,author=mangaAuthor,user_id=current_user.id)
            db.session.add(new_manga)
            db.session.commit()
            flash('Manga added sucessfully',category='success')

    return render_template("index.html",user=current_user)

@views.route('/about')
def about():
    return render_template("about.html",user=current_user)