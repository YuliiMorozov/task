from flask import jsonify
from indication import app
from indication.models.user import User


@app.route("/api/home", methods=["GET"])
def api_home():
    user = User.query.filter_by(username=User.username).first()
    return jsonify({"msg": "Welcome to home page, " + user.username}), 200