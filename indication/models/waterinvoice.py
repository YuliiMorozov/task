from indication import db

class WaterInvoice(db.Model):
    __tablename__ = "water_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_water = db.Column(db.Float, unique=False)

    water_invoices_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))

    # invoices = db.relationship('Invoice', backref='water_invoice', lazy='dynamic')

    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))