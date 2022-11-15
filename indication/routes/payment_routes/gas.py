from indication import app
from indication.controllers import gas_information

@app.route('/payment/gas')
def gas():
    return gas_information()