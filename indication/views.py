from flask import render_template, request, redirect
from indication import db
from indication.models import ElectricityInvoice, GasInvoice, House, Flat, WaterInvoice, Invoice
from indication.forms import FormGeneral

def create_data():

    form_general = FormGeneral()
    if request.method == "POST":

        house_number = request.form['house']
        flat_number = request.form['flat']
        count_water = request.form['water']
        count_gas = request.form['gas']
        count_electricity = request.form['electricity']

        house = House(house_number=house_number)
        flat = Flat(flat_number=flat_number, house=house)        
        water_invoice = WaterInvoice(count_water=count_water)
        gas_invoice = GasInvoice(count_gas=count_gas)
        electricity_invoice = ElectricityInvoice(count_electricity=count_electricity)

        invoice = Invoice(flat=flat, water_invoice=water_invoice, gas_invoice=gas_invoice, electricity_invoice=electricity_invoice)

        try:
            db.session.add(house)
            db.session.add(flat)            
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
                                

def pay_information():
    waterinvoice = WaterInvoice.query.all()
    gasinvoice = GasInvoice.query.all()
    electricityinvoice = ElectricityInvoice.query.all()
    houseid = Flat.query.all() 
    return render_template("payment.html",
                            waterinvoice=waterinvoice,
                            gasinvoice=gasinvoice,
                            electricityinvoice=electricityinvoice,
                            houseid=houseid)

def water_information():
    water = WaterInvoice.query.all()
    return render_template("water.html",
                            water=water)

def gas_information():
    gas = GasInvoice.query.all()
    return render_template("gas.html",
                            gas=gas)

def electricity_information():
    electricity = ElectricityInvoice.query.all()
    return render_template("electricity.html",
                            electricity=electricity)