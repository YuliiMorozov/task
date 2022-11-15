from flask import render_template, request, redirect
from indication import db
from indication.forms import FormGeneral
from indication.models import House, Flat, Invoice, WaterInvoice, GasInvoice, ElectricityInvoice


def create_data():

    form_general = FormGeneral()
    form_general.house.choices = [(house.id, house.house_number) for house in House.query.order_by(House.house_number).all()]
    form_general.flat.choices = [(flat.id, flat.flat_number) for flat in Flat.query.filter_by(house_id=House.flats).all()]

    if request.method == "POST":


        flat_id = request.form['flat']
        count_water = request.form['water']
        count_gas = request.form['gas']
        count_electricity = request.form['electricity']        
 
            
        flat = Flat.query.filter_by(id=flat_id).first()    

        invoice = Invoice(flat=flat)
        water_invoice = WaterInvoice(count_water=count_water, invoice=invoice, flat=flat)
        gas_invoice = GasInvoice(count_gas=count_gas, invoice=invoice, flat=flat)
        electricity_invoice = ElectricityInvoice(count_electricity=count_electricity, invoice=invoice, flat=flat)

        try:            
            db.session.add(water_invoice)
            db.session.add(gas_invoice)
            db.session.add(electricity_invoice)
            db.session.add(invoice)
            db.session.commit()
            return redirect('/create_payment')
        except:
            return "Error! Make sure the forms are filled out correctly."
    else:
        return render_template("create_payment.html",
                                template_form=form_general)