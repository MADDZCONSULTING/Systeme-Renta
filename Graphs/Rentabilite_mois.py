
from flask import jsonify
from  flask_restful import  Resource, request

class RentabiliteMois(Resource):

    def get(self):
     #initialisation
     Mois=[ 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
        'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
     rentabilite=[550000,649800,703200,604300,509900,459080,78760,800320,812200]
     commissions=[200,220,190,240,210,180,185,195,205]
     demande_passee= [5500,6498,7032,6043,5099,4598,7876,8032,8122]
     demande_future = [5000, 6390, 6899, 6980, 7109, 5809, 6897, 7078, 8422]
     performance_bon=[155, 100, 189, 207, 266, 243, 230, 248, 254]
     performance_moyen=[302, 345, 378, 379, 401, 411, 437, 431, 427]
     perfomance_mauvais=[243,255, 133,114,33, 46, 33, 21, 19]



     response= jsonify(data=(Mois,rentabilite,commissions,demande_passee,demande_future,performance_bon,
                             performance_moyen,perfomance_mauvais))
     response.headers.add('Access-Control-Allow-Origin', '*')
     return response

