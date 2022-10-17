from flask import render_template, request, redirect
from indication import db
from indication.models import *
from indication.forms import *
from cloudipsp import Api, Checkout

# def func_for_class()


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

        
        # water_invoice = WaterInvoice(count_water=count_water)
        # gas_invoice = GasInvoice(count_gas=count_gas)
        # electricity_invoice = ElectricityInvoice(count_electricity=count_electricity)
        # invoice = Invoice(flat=flat, water_invoice=water_invoice, gas_invoice=gas_invoice, electricity_invoice=electricity_invoice)

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


def pay_information():
    houses = House.query.all()
    flats = Flat.query.all()
    invoices = Invoice.query.all()
    waterinvoices = WaterInvoice.query.all()
    gasinvoices = GasInvoice.query.all()
    electricityinvoices = ElectricityInvoice.query.all()
    users = User.query.all()
    return render_template("payment.html",
                            houses=houses,
                            flats=flats,
                            invoices=invoices,
                            waterinvoices=waterinvoices,
                            gasinvoices=gasinvoices,
                            electricityinvoices=electricityinvoices,
                            users=users)



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

def to_pay():
    # sum = class.query.get()
    api = Api(merchant_id=1396424,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "UAH",
        "amount": str(100) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)



def rest():
    return "Hello"