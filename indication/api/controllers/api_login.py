from indication import app
from flask import request, jsonify
from indication.models.user import User
import jwt


def api_login_controller():
    username = request.json.get("username")   
    password = request.json.get("password")
    role =  request.json.get("role")
    
    user = User.query.filter_by(username=username).first()

    errors = []
    
    if user is None:
        errors.append("Bad username or password")
        # return jsonify({"msg": "Bad username or password"}), 400

    # if username != user.username or user.check_password(password) is False:
    #     errors.append("Bad username or password2")
        # return jsonify({"msg": "Bad username or password"}), 400
    
    if errors:
        return jsonify({"status": "fail",
                        "detail": errors[0]}), 400  
    
    else:


        errors.append("Welcome to the website")
            
        access_token = jwt.encode({"username": username, "role": role}, app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"status": "success",
                    "detail": errors[0],
                    "access_token": access_token})