from app import db


class ChargeFixeUpdated(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False, unique=True)
    charge_restante = db.Column(db.Integer, nullable=False, unique=False)
    demande_restante = db.Column(db.Integer, nullable=False, unique=False)


def __init__(self, date, charge_restante, demande_restante):
    self.date = date
    self.charge_restante = charge_restante
    self.demande_restante = demande_restante
