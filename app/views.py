from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from . import db
import json

from .models import Manga

views = Blueprint('views',__name__)

@views.route('/',methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        print(request)
        manga_name = request.form.get('mangaName')
        mangaAuthor = request.form.get('mangaAuthor')
        print("bahahahaha")
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

@views.route('/delete-manga', methods=['POST'])
def delete_note():
    manga = json.loads(request.data)
    mangaID = manga['mangaId']
    manmga_to_delete = Manga.query.get(mangaID)
    if manmga_to_delete:
        if manmga_to_delete.user_id == current_user.id:
            db.session.delete(manmga_to_delete)
            db.session.commit()

    return jsonify({})

@views.route('/about')
def about():
    return render_template("about.html",user=current_user)

@views.route('/detail/<id>')
def detail(id):
    manga = Manga.query.filter_by(id=id).first()
    return render_template("details.html",user=current_user,manga=manga)