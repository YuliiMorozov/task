from flask import jsonify
from indication import ma
from indication.models.flat import Flat

class FlatSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Flat    
    id = ma.auto_field()
    flat_number = ma.auto_field()

def get_flats(house_id):
  
    flats = Flat.query.filter_by(house_id=house_id)    
    flat_data = FlatSchema(many=True).dump(flats)
    return jsonify(flat_data), 200