from indication import db

class GasInvoice(db.Model):
    __tablename__ = "gas_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_gas = db.Column(db.Float, unique=False)

    invoices = db.relationship('Invoice', backref='gas_invoice', lazy='dynamic')