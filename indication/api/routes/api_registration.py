from indication import app
from indication.api.controllers.api_registration import api_registration_controller

@app.route("/api/registration", methods=["POST"])
def api_registration():
    return api_registration_controller()