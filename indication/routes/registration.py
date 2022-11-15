from indication import app
from indication.controllers.registration import create_registration


@app.route('/registration', methods=["GET", "POST"])
def registration():
    return create_registration()