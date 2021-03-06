from datetime import datetime

from flask import Flask
from flask_cors import CORS
from  flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from APIs.rentabilite_checking import calculRentabilite
from Graphs.Rentabilite_mois import RentabiliteMois
from Graphs.Rentabilite_jour import RentabiliteJour
from Graphs.simulation import Simulation
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)
#add database
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:easyrelay2021@localhost/chargefixe'
app.config['SECRET_KEY']="Secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initailize the db
db = SQLAlchemy(app)

from application_layer.charge_test import charge_fixe_update
from APIs.charge_fixe_jour import  Charge

from models.chargeFixeUpdated import ChargeFixeUpdated

#Adding APIs
api= Api(app)
api.add_resource(calculRentabilite,"/rentabilite")
api.add_resource(Charge,"/chargefixe")
api.add_resource(RentabiliteMois,"/RentabiliteMoisTest")
api.add_resource(RentabiliteJour,"/RentabiliteJourTest")
api.add_resource(Simulation,"/simulation")



#schedule jobs
sched = BackgroundScheduler(daemon=True)
sched.add_job(charge_fixe_update,'cron',hour='12',minute='35')
sched.start()

#today = datetime.today().date()
#charge= ChargeFixeUpdated(date=today, charge_restante=20000, demande_restante=200)
#db.session.add(charge)
#db.session.commit()


if __name__ == '__main__':
    app.run()

