from indication import db
from flask import request, jsonify
from indication.models import House, Flat, ElectricityInvoice, GasInvoice, Invoice, WaterInvoice

def api_create_payment_controller():
    
    house_number = request.json.get("house_number")
    flat_number = request.json.get("flat_number")
    invoice = request.json.get("invoice")    
    count_water = request.json.get("count_water")
    count_gas = request.json.get("count_gas")
    count_electricity = request.json.get("count_electricity")

    house = House.query.filter_by(house_number=house_number).first()
    flat = Flat.query.filter_by(flat_number=flat_number, house=house).first()

    errors = []  

    if house is None:         
        errors.append("Error, house not chosen")

    if flat is None:
        errors.append("Error, flat not chosen")      

    if count_water.isnumeric() is False and float(count_water) < 0:
        errors.append("Error when transmitting water meter readings")       

    if count_gas.isnumeric() is False and float(count_gas) < 0:
        errors.append("Error when transmitting gas meter readings")       
    
    if count_electricity.isnumeric() is False and float(count_electricity) < 0:
        errors.append("Error when transmitting electricity meter readings")        
   
    if errors:
        return jsonify({"status": "fail",
                        "detail": errors}), 400  

    invoice = Invoice(flat=flat)
    water_invoice = WaterInvoice(count_water=count_water, invoice=invoice, flat=flat)
    gas_invoice = GasInvoice(count_gas=count_gas, invoice=invoice, flat=flat)
    electricity_invoice = ElectricityInvoice(count_electricity=count_electricity, invoice=invoice, flat=flat)

    db.session.add(water_invoice)
    db.session.add(gas_invoice)
    db.session.add(electricity_invoice)
    db.session.add(invoice)
    db.session.commit()

    errors.append("Your meter readings have been taken")
    
    return jsonify({"status": "success",
                    "detail": errors}), 200