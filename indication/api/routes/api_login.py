from indication import app
from indication.api.controllers.api_login import api_login_controller


@app.route("/api/login", methods=["POST"])
def api_login():
    return api_login_controller()