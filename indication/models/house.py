from indication import db

class House(db.Model):    
    __tablename__ = 'house'
    id = db.Column(db.Integer, primary_key=True)
    house_number = db.Column(db.Integer, unique=False)

    flats = db.relationship('Flat', backref='house', lazy='dynamic')

    # def __repr__(self):
        # return f"<house {self.id}>"