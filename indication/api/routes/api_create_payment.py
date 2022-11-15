from indication import app
from indication.api.controllers.api_create_payment import api_create_payment_controller


@app.route("/api/create_payment", methods=["POST"])
def api_create_payment():
    return api_create_payment_controller()