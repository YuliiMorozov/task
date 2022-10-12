from indication import db

class ElectricityInvoice(db.Model):
    __tablename__ = "electricity_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_electricity = db.Column(db.Float, unique=False)

    electricity_invoices_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))

    # invoices = db.relationship('Invoice', backref='electricity_invoice', lazy='dynamic')
    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))