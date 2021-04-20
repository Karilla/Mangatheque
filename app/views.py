from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route('/')
def home():
    print("yo")
    return render_template("index.html")

@views.route('/about')
def about():
    return render_template("about.html")