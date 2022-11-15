from flask import request, jsonify
import re
from indication.models.user import User
from indication import db

def api_registration_controller():

    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")
    password2 = request.json.get("password2")   

    new_username = User.query.filter_by(username=username).first()
    new_email = User.query.filter_by(email=email).first()

    regexForEmail = '[A-Za-z0-9._-]+@[a-z.-]+.[A-Z|a-z]'
    regexForPassword = '[a-z]+[a-z]+[a-z]+.+.+.+.'

    # check username
    if len(username) < 4 or len(username) > 25:
        return jsonify({"msg": "Name of username is short"}), 400
    elif new_username:        
        return jsonify({"msg": "User with this username already exists"}), 400

    # check email
    elif bool(re.fullmatch(regexForEmail, email)) is False:
        return jsonify({"msg": "Please enter a valid email"}), 400
    elif new_email:
        return jsonify({"msg": "This email has already used"}), 400

    # check password
    elif len(password) < 7:
        return jsonify({"msg": "Password is short"}), 400
    elif bool(re.fullmatch(regexForPassword, password)) is False:
        return jsonify({"msg": "Please enter a valid password"}), 400
    elif password2 != password:
        return jsonify({"msg": "Please repeat the password correctly"}), 400
    else:
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "Welcome to website"}), 200