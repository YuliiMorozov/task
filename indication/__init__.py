from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

from .admin.admin import admin


app = Flask(__name__)

# This string is a way to protect against CSRF or cross-site document forgery.
app.config["SECRET_KEY"] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(admin, url_prefix='/admin')

# create login manager
# login_manager = LoginManager()
# login_manager.init_app(app)

from indication import urls

db.create_all()