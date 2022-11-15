from indication import app
from indication.api.controllers.api_payment import api_houses_controller
from indication.api.controllers.flat import get_flats

@app.route("/api/house", methods=["GET"])
def api_houses():
    return api_houses_controller()

@app.route("/api/house/<int:house_id>", methods=["GET"])
def flats(house_id):
    return get_flats(house_id)