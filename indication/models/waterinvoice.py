from indication import db

class WaterInvoice(db.Model):
    __tablename__ = "water_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_water = db.Column(db.Float, unique=False)

    invoices = db.relationship('Invoice', backref='water_invoice', lazy='dynamic')