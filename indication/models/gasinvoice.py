from indication import db

class GasInvoice(db.Model):
    __tablename__ = "gas_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_gas = db.Column(db.Float, unique=False)

    gas_invoices_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))

    # invoices = db.relationship('Invoice', backref='gas_invoice', lazy='dynamic')
    flat_id = db.Column(db.Integer, db.ForeignKey('flat.id'))