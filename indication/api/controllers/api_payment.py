from flask import jsonify
from indication import ma
from indication.models import House

class HouseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = House    
    id = ma.auto_field()
    house_number = ma.auto_field()


def api_houses_controller():    
    houses = House.query.all()    
    house_data = HouseSchema(many=True).dump(houses)
    return jsonify(house_data), 200