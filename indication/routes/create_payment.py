from indication import app
from indication.controllers.create_payment import create_data

@app.route('/create_payment', methods=["GET", "POST"])
def create_payment():
    return create_data() 