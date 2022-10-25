from flask import render_template
from indication.models import GasInvoice

# class Gas 
    # __init__()
    # manipulation with gas

def gas_information():
    gas = GasInvoice.query.all()
    return render_template("gas.html",
                            gas=gas)