from indication import db

class ElectricityInvoice(db.Model):
    __tablename__ = "electricity_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_electricity = db.Column(db.Float, unique=False)

    invoices = db.relationship('Invoice', backref='electricity_invoice', lazy='dynamic')