from indication import app
from indication.controllers.payment import pay_information

@app.route('/payment')
def payment():
    return pay_information()