from indication import app
from indication.models.flat import Flat
from flask import jsonify

# create a json 
@app.route('/flat/<house_id>')
def flatbyhouse(house_id):
    flat = Flat.query.filter_by(house_id=house_id).all()
    flatArray = []
    for item in flat:
        flatObj = {}
        flatObj['id'] = item.id
        flatObj['flat_number'] = item.flat_number
        flatArray.append(flatObj)
    return jsonify({'flathouse' : flatArray})