from indication import app
from indication.controllers import water_information

@app.route('/payment/water')
def water():
    return water_information()