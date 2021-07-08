from calendar import monthrange
from datetime import date, timedelta, datetime
from app import db
from models.chargeFixeSaved import ChargeFixeSaved
from models.chargeFixeUpdated import ChargeFixeUpdated


def last_day_of_month(date_value):
    return date_value.replace(day=monthrange(date_value.year, date_value.month)[1])


def charge_fixe_update():
    print("hola")
    today = datetime.today().date()
    tomorrow = datetime.now() + timedelta(1)
    if (today == last_day_of_month(today)):
        # ramener la charge fixe de la bdd de mois
        next_month= (datetime.now().month+1) % 12
        charge_mois = ChargeFixeSaved.query.filter(ChargeFixeSaved.id == next_month).first().charge_fixe
        #call api demande mois prévue
        demande_mois=0
        #initialiser la nouvelle ligne du mois prochain
        charge_mois=ChargeFixeUpdated(date=tomorrow,charge_restante=charge_mois,demande_restante=demande_mois)
        print("hola")
        db.session.add(charge_mois)
        db.session.commit()

    else:
        # call apis
        demande_prevue = 0
        demande_reelle = 0
        charge_livraison = 0

        charge = ChargeFixeUpdated.query.filter(ChargeFixeUpdated.date == date.today()).first()
        charge_restante=charge.charge_restante - ((charge_livraison * demande_prevue) - (
                        (demande_prevue - demande_reelle) * charge_livraison))
        demande_restante= charge.demande_restante - demande_reelle
        if (charge_restante>0 ):
           nouvelle_charge=ChargeFixeUpdated(date=tomorrow,charge_restante=charge_restante,demande_restante=demande_restante)

        else:
            nouvelle_charge=ChargeFixeUpdated(date=tomorrow,charge_restante=0,demande_restante=1)
        db.session.add(nouvelle_charge)
        db.session.commit()
        print(charge)