from flask import render_template, redirect
from indication.models import House, Flat, Invoice, WaterInvoice, GasInvoice, ElectricityInvoice, User
from cloudipsp import Api, Checkout


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