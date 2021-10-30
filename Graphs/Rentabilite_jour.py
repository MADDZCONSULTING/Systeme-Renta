
from flask import jsonify
from  flask_restful import  Resource
import json


class RentabiliteJour(Resource):

    def get(self):
     #initialisation
     jours=[ 'Samedi','Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi']
     #Récupérer à partir d'un fichier
     with open('./Data/simulation.json', 'r', encoding='cp437') as file:
         data1 = file.read()
     display_data= json.loads(data1)

     response= jsonify(data=(jours,display_data[0],display_data[1],display_data[2],display_data[3]))
     response.headers.add('Access-Control-Allow-Origin', '*')
     return response
