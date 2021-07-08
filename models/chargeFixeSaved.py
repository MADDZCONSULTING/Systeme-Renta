from app import db


class ChargeFixeSaved(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mois = db.Column(db.String(25), nullable=False, unique=True)
    charge_fixe = db.Column(db.Integer, nullable=False, unique=False)

def __init__(self, id, mois, charge_fixe):
    self.id = id
    self.mois = mois
    self.charge_fixe = charge_fixe