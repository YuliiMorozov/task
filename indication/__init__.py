from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# This string is a way to protect against CSRF or cross-site document forgery.
app.config["SECRET_KEY"] = "my_secret"

from indication import models, urls, forms

db.create_all()