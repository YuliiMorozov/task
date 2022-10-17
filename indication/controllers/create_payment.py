from flask import render_template, request, redirect
from indication import db
from indication.forms import FormGeneral
from indication.models import House, Flat, Invoice, WaterInvoice, GasInvoice, ElectricityInvoice


def create_data():

    form_general = FormGeneral()
    if request.method == "POST":

        house_number = request.form['house']
        flat_number = request.form['flat']
        count_water = request.form['water']
        count_gas = request.form['gas']
        count_electricity = request.form['electricity']

         
        house = House.query.filter_by(house_number=house_number).first()    
        if house is None:
            house = House(house_number=house_number)        
            db.session.add(house)
            
        flat = Flat.query.filter_by(flat_number=flat_number, house=house).first()    
        if flat is None:
            flat = Flat(flat_number=flat_number, house=house)        
            db.session.add(flat)

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