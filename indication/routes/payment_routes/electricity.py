from indication import app
from indication.controllers import electricity_information

@app.route('/payment/electricity')
def electricity():
    return electricity_information()