from datetime import datetime
from  flask_restful import  Resource
from models.chargeFixeUpdated import ChargeFixeUpdated


class Charge(Resource):

    def post(self):
        today = datetime.today().date()
        charge = ChargeFixeUpdated.query.filter(ChargeFixeUpdated.date == today).first()
        charge_jour = charge.charge_restante / charge.demande_restante

        return (charge_jour)
