from flask import jsonify
from indication.models import WaterInvoice, GasInvoice, ElectricityInvoice, Flat

def get_indications(flat_id):

    flat = Flat.query.filter_by(id=flat_id).all()
    water = WaterInvoice.query.filter_by(flat_id=flat_id).order_by(WaterInvoice.id.desc()).limit(2)
    gas = GasInvoice.query.filter_by(flat_id=flat_id).order_by(GasInvoice.id.desc()).limit(2)
    electricity = ElectricityInvoice.query.filter_by(flat_id=flat_id).order_by(ElectricityInvoice.id.desc()).limit(2)

    if flat == []:
        return jsonify({"Error": "This apartment does not exist"}), 404

    water_payment_order = {
        "past_water_value": "No water data",
        "now_water_value": "No water data"
    }

    gas_payment_order = {
        "past_gas_value": "No gas data",
        "now_gas_value": "No gas data"
    }
    electricity_payment_order = {
        "past_electricity_value": "No electricity data",
        "now_electricity_value": "No electricity data"
    }

    invoice = [water_payment_order, gas_payment_order, electricity_payment_order]

    water_price = gas_price = electricity_price = 0



    if len(water[:]) == 1:
        water_price = water[-1].count_water
        water_payment_order["now_water_value"] = water[-1].count_water

    elif len(water[:]) >= 2:
        water_price = water[-1].count_water - water[-2].count_water
        water_payment_order["past_water_value"] = water[-2].count_water
        water_payment_order["now_water_value"] = water[-1].count_water 

    water_payment_order["to_pay_for_water"] = (water_price * 100)


    if len(gas[:]) == 1:
        gas_price = gas[-1].count_gas
        gas_payment_order["now_gas_value"] = gas[-1].count_gas

    elif len(gas[:]) >= 2:
        gas_price = gas[-1].count_gas - gas[-2].count_gas
        gas_payment_order["past_gas_value"] = gas[-2].count_gas
        gas_payment_order["now_gas_value"] = gas[-1].count_gas
   
    gas_payment_order["to_pay_for_gas"] = (gas_price * 100)


    if len(electricity[:]) == 1:
        electricity_price = electricity[-1].count_electricity
        electricity_payment_order["now_electricity_value"] = electricity[-1].count_electricity

    elif len(electricity[:]) >= 2:
        electricity_price = electricity[-1].count_electricity - electricity[-2].count_electricity
        electricity_payment_order["past_electricity_value"] = electricity[-2].count_electricity
        electricity_payment_order["now_electricity_value"] = electricity[-1].count_electricity   

    electricity_payment_order["to_pay_for_electricity"] = (electricity_price * 100)
    
    return jsonify(invoice), 200