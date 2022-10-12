from indication import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = "invoice"
    id = db.Column(db.Integer, primary_key=True)

    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))
    water_invoices = db.relationship('WaterInvoice', backref='invoice', lazy='dynamic')
    gas_invoices = db.relationship('GasInvoice', backref='invoice', lazy='dynamic')
    electricity_invoices = db.relationship('ElectricityInvoice', backref='invoice', lazy='dynamic')

    # water_invoice_id = db.Column(db.Integer, db.ForeignKey('water_invoice.id'))
    # gas_invoice_id = db.Column(db.Integer, db.ForeignKey('gas_invoice.id'))
    # electricity_invoice_id = db.Column(db.Integer, db.ForeignKey('electricity_invoice.id'))

    date = db.Column(db.DateTime, default=datetime.utcnow)