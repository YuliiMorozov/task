from indication import db

class Flat(db.Model):
    __tablename__ = 'flat'
    id = db.Column(db.Integer, primary_key=True)    
    flat_number = db.Column(db.Integer, unique=False)

    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    invoices = db.relationship('Invoice', backref='flat', lazy='dynamic')

    # relationships with invoices
    water_invoices = db.relationship('WaterInvoice', backref='flat', lazy='dynamic')
    gas_invoices = db.relationship('GasInvoice', backref='flat', lazy='dynamic')
    electricity_invoices = db.relationship('ElectricityInvoice', backref='flat', lazy='dynamic')

    # def __repr__(self):
        # return f"<flat {self.id}>"