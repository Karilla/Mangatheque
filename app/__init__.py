from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_assets import Environment, Bundle
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app(secret_key):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    #assets = Environment()
    #assets.init_app(app)

    #css = Bundle('static/css/*.css', filters='postcss', output='dist/css/main.css')
    #assets.register('css', css)

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Manga, Tome

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('app/' + DB_NAME):
        db.create_all(app=app)
        print("database created")