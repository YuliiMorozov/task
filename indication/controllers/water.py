from flask import render_template
from indication.models import WaterInvoice

def water_information():
    water = WaterInvoice.query.all()
    return render_template("water.html",
                            water=water)