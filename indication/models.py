from indication import db


class House(db.Model):    
    __tablename__ = 'house'
    id = db.Column(db.Integer, primary_key=True)
    house_number = db.Column(db.Integer, unique=False)
    flats = db.relationship('Flat', backref='house', lazy='dynamic')

    def __repr__(self):
        return f"<house {self.id}>"


class Flat(db.Model):
    __tablename__ = 'flat'
    id = db.Column(db.Integer, primary_key=True)    
    flat_number = db.Column(db.Integer, unique=False)

    house_id = db.Column(db.Integer, db.ForeignKey('house.id'))
    invoices = db.relationship('Invoice', backref='flat', lazy='dynamic')

    def __repr__(self):
        return f"<flat {self.id}>"


class Invoice(db.Model):
    __tablename__ = "invoice"
    id = db.Column(db.Integer, primary_key=True)

    flat_id =  db.Column(db.Integer, db.ForeignKey('flat.id'))

    # waterinvoices = db.relationship('WaterInvoice', backref='invoice', lazy='dynamic')
    # gasinvoices = db.relationship('GasInvoice', backref='invoice', lazy='dynamic')
    # flats = db.relationship('Flat', backref='house', lazy='dynamic')
    # flats = db.relationship('Flat', backref='house', lazy='dynamic')

    
    
    
    # electricity_invoice_id = db.Column(db.Float, db.ForeignKey('electricity_invoice.id'))


class WaterInvoice(db.Model):
    __tablename__ = "water_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_water = db.Column(db.Float, unique=False)

    # water_invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))


class GasInvoice(db.Model):
    __tablename__ = "gas_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_gas = db.Column(db.Float, unique=False)

    # gas_invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'))


class ElectricityInvoice(db.Model):
    __tablename__ = "electricity_invoice"
    id = db.Column(db.Integer, primary_key=True)
    count_electricity = db.Column(db.Float, unique=False)