from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FormGeneral(FlaskForm):
    house = StringField("Enter house number:", render_kw={"placeholder": "11"})    
    flat = StringField("Enter the apartment number:", render_kw={"placeholder": "119"})
    water = StringField("Water meter readings:", render_kw={"placeholder": "00000.00"})
    gas = StringField("Gas meter readings:", render_kw={"placeholder": "00000.00"})
    electricity = StringField("Electricity meter readings:", render_kw={"placeholder": "00000.00"})
    submit = SubmitField("Send")