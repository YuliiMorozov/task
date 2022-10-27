from importlib.resources import read_text
from flask import render_template, request, redirect, url_for, flash, jsonify, request, make_response
from indication import app, db, login_manager
import indication
# from indication.middleware.check_token import Middleware
# from indication.middleware.check_token import Middleware
from .controllers import create_data, pay_information, water_information, gas_information, electricity_information, to_pay, create_registration, create_login
from indication.models.user import *
from indication.models.flat import *
from indication.models.house import *

import datetime
from indication.forms import LoginForm
import jwt
from flask_jwt_extended import create_access_token

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import re

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
# jwt = JWTManager(app)

# from indication.middleware.check_token import Middleware
# from werkzeug.wrappers import Request, Response


# class Middleware():
#     def __init__(self, app):
#         print('init')
#         self.app = app
#         self.username = 'TestUser'
#         self.password = 'TestPass'

#     def __call__(self, environ, start_response):
#         print("aaaa")
#         request = Request(environ)
#         username = request.authorization['username']
#         password = request.authorization['password']

#         if username == self.username and password == self.password:
#             environ['user'] = {
#                 'name': 'Test User'
#             }

#             return self.app(environ, start_response)

#         res = Response('Authorization failed', mimetype='text/plain', status=401)
#         return res(environ, start_response)

# app.wsgi_app = Middleware(app.wsgi_app)



# app.wsgi_app = Middleware(app.wsgi_app)

from flask_login import current_user, login_required, login_user, logout_user
# from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# @app.get('/admin')
# def admin():
#     return render_template('admin.html')

admin = Admin(app, name='Create house & flat', template_mode='bootstrap3')
admin.add_view(ModelView(House, db.session, name='Add house number'))
admin.add_view(ModelView(Flat, db.session, name='Add flat number'))


@app.route("/api/login", methods=["POST"])
def login_test():
    username = request.json.get("username", None)   
    password = request.json.get("password", None)   
    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({"msg": "Bad username or password"}), 400

    if username != user.username or user.check_password(password) is False:
        return jsonify({"msg": "Bad username or password"}), 400
        
    access_token = jwt.encode({"username": username}, app.config["SECRET_KEY"], algorithm="HS256")
    return jsonify(access_token=access_token)



@app.route("/api/registration", methods=["POST"])
def api_registration():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    password2 = request.json.get("password2")   

    newUsername = User.query.filter_by(username=username).first()
    newEmail = User.query.filter_by(email=email).first()

    regexForEmail = '[A-Za-z0-9._-]+@[a-z.-]+.[A-Z|a-z]'
    regexForPassword = '[A-Z]+[a-z]+[0-9]+.+.+.+.'

    # check username
    if len(username) < 4 or len(username) > 25:
        return jsonify({"msg": "Name of username is short"}), 400

    elif newUsername:
        return jsonify({"msg": "User with this username already exists"}), 400

    # check email
    # need create func to check email addres
    elif bool(re.fullmatch(regexForEmail, email)) is False:
        return jsonify({"msg": "Please enter a valid email"}), 400

    elif newEmail:
        return jsonify({"msg": "This email has already used"}), 400


    # check password
    # need create func to check password
    elif bool(re.fullmatch(regexForPassword, password)) is False:
        return jsonify({"msg": "Please enter a valid password"}), 400

    elif password2 != password:
        return jsonify({"msg": "Please repeat the password correctly"}), 400

    else:
        return jsonify({"msg": "Welcome to website"}), 200





    # regexForEmail = '[A-Za-z0-9._-]+@[a-z.-]+.[A-Z|a-z]'
    # regexForPassword = '[A-Z]+[a-z]+[0-9]+.+.+.+.'

    # # check username
    # if len(username) < 4 or len(username) > 25:
    #     return jsonify({"msg": "Name of username is short"}), 400

    # elif newUsername:
    #     return jsonify({"msg": "User with this username already exists"}), 400

    # else:
    #     return jsonify({"msg": "This username is free"}), 200

    # # check email
    # # need create func to check email addres
    # if bool(re.fullmatch(regexForEmail, email)) is False:
    #     return jsonify({"msg": "Please enter a valid email"}), 400

    # elif newEmail:
    #     return jsonify({"msg": "This email has already used"}), 400

    # else:
    #     return jsonify({"msg": "This email is suitable for registration"}), 200

    # # check password
    # # need create func to check password
    # if bool(re.fullmatch(regexForPassword, password)) is False:
    #     return jsonify({"msg": "Please enter a valid password"}), 400

    # elif password2 != password:
    #     return jsonify({"msg": "Please repeat the password correctly"}), 400

    # else:
    #     return jsonify({"msg": "Good password"}), 200



@app.route("/api/home", methods=["GET"])
def api_home():

    username = "Yulii"
    return jsonify({"msg": "Welcome to home page, " + username}), 200





@app.route('/api/<username_id>')
def user(username_id):
    user = User.query.filter_by(id=username_id).all()
    userArray = []
    for item in user:
        userObj = {}
        userObj['id'] = item.id
        userObj['username'] = item.username
        userObj['email'] = item.email
        userObj['password_hash'] = item.password_hash
        userObj['joined_at'] = item.joined_at
        userArray.append(userObj)
    return jsonify({'USERS' : userArray})







@app.route('/registration', methods=["GET", "POST"])
def registration():
    return create_registration()

# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=['GET','POST'])
def login():
    return create_login()

@app.route('/')
@app.route('/home')
# @login_required
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
# @login_required
def create_payment():
    return create_data()    

@app.route('/payment')
@login_required
def payment():
    return pay_information()

@app.route('/payment/<float:sum>')
@login_required
def item_buy(sum):
    return to_pay()

@app.route('/payment/water')
def water():
    return water_information()

@app.route('/payment/gas')
def gas():
    return gas_information()

@app.route('/payment/electricity')
def electricity():
    return electricity_information()

@app.route('/about')
def about():
    return render_template("about.html")

# a decorator here to handle unauthorized users:
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# @app.after_request
# def redirect_to_signin(response):
#     if response.status_code == 401:
#         return redirect(url_for('login') + '?next=' + request.url)

#     return response

# create a json 
@app.route('/flat/<house_id>')
def flatbyhouse(house_id):
    flat = Flat.query.filter_by(house_id=house_id).all()
    flatArray = []
    for item in flat:
        flatObj = {}
        flatObj['id'] = item.id
        flatObj['flat_number'] = item.flat_number
        flatArray.append(flatObj)
    return jsonify({'flathouse' : flatArray})