from flask import render_template, redirect
from indication import app
from indication.views import create_data, pay_information, water_information, gas_information, electricity_information

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/create_payment', methods=["GET", "POST"])
def create_payment():
    return create_data()    

@app.route('/payment')
def payment():
    return pay_information()

@app.route('/payment/water')
def water():
    return water_information()

@app.route('/payment/gas')
def gas():
    return gas_information()

@app.route('/payment/electricity')
def electricity():
    return electricity_information()

@app.route('/about')
def about():
    return render_template("about.html")
