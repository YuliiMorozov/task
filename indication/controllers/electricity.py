from flask import render_template
from indication.models import ElectricityInvoice

def electricity_information():
    electricity = ElectricityInvoice.query.all()
    return render_template("electricity.html",
                            electricity=electricity)