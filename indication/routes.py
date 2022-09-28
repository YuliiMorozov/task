from flask import render_template, request, redirect

from indication import app, db
from indication.models import ElectricityInvoice, GasInvoice, House, Flat, WaterInvoice
from indication.forms import FormGeneral


# This string is a way to protect against CSRF or cross-site document forgery.
app.config["SECRET_KEY"] = "my_secret"

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
def create_payment():

    form_general = FormGeneral()
    if request.method == "POST":
        house_number = request.form['house']
        flat_number = request.form['flat']
        count_water = request.form['water']
        count_gas = request.form['gas']
        count_electricity = request.form['electricity']


        house = House(house_number=house_number)
        flat = Flat(flat_number=flat_number)
        water_invoice = WaterInvoice(count_water=count_water)
        gas_invoice = GasInvoice(count_gas=count_gas)
        electricity_invoice = ElectricityInvoice(count_electricity=count_electricity)


        try:
            db.session.add(house)
            db.session.add(flat)
            db.session.add(water_invoice)
            db.session.add(gas_invoice)
            db.session.add(electricity_invoice)
            db.session.commit()
            return redirect('/create_payment')
        except:
            return "Error! Make sure the forms are filled out correctly."
    else:
        return render_template("create_payment.html",
                                template_form=form_general)



@app.route('/payment')
def payment():
    waterinvoice = WaterInvoice.query.all()
    gasinvoice = GasInvoice.query.all()
    electricityinvoice = ElectricityInvoice.query.all()
    houseid = Flat.query.all() 
    return render_template("payment.html",
                            waterinvoice=waterinvoice,
                            gasinvoice=gasinvoice,
                            electricityinvoice=electricityinvoice,
                            houseid=houseid)



@app.route('/payment/water')
def water():
    water = WaterInvoice.query.all()
    return render_template("water.html",
                            water=water)


@app.route('/payment/gas')
def gas():
    gas = GasInvoice.query.all()
    return render_template("gas.html",
                            gas=gas)


@app.route('/payment/electricity')
def electricity():
    electricity = ElectricityInvoice.query.all()
    return render_template("electricity.html",
                            electricity=electricity)


@app.route('/about')
def about():
    return render_template("about.html")
