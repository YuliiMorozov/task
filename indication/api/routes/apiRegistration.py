from flask import render_template, request, redirect, url_for, flash, jsonify, request, make_response
from indication import app, db, login_manager
import indication
from indication.models.user import *
from indication.models.flat import *
from indication.models.house import *
import jwt
import datetime
from indication.forms import LoginForm
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import re


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



