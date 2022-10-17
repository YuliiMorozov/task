from flask import render_template
from indication.models import GasInvoice

def gas_information():
    gas = GasInvoice.query.all()
    return render_template("gas.html",
                            gas=gas)