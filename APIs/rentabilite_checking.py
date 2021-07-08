import json
from datetime import date
from flask import jsonify
from  flask_restful import  Resource, request
import requests

from models.livraison import LivraisonSchema
from models.tournee import TourneeSchema


class calculRentabilite(Resource):

    def post(self):
     #initialisation
     liste_rentabilite=[]
     tournee_rentable=0
     tournee_non_rentable=0


     today=date.today()
     print(today)
     url = "https://dev.easy-relay.com/api/mob2/api.php?action=getTourneeDay&"+"day=2021-02-07"+"&etat=3&type=l"

     payload = {}
     headers = {
         'email': 'dm@er.com',
         'mdp': 'test'
     }

     response = requests.request("GET", url, headers=headers, data=payload)
     tournees= response.json()
     print(tournees)
     for tournee in tournees:
         schema = TourneeSchema()
         result = schema.load(tournee)# deserialize the object
         id_tournee=result.idTournee
         url = "https://dev.easy-relay.com/api/mob2/api.php?action=getLvTournee&id_tournee="+id_tournee

         payload = {}
         headers = {
             'email': 'dm@er.com',
             'mdp': 'test'
         }

         response_livraisons = requests.request("GET", url, headers=headers, data=payload)
         liste_livraison=response_livraisons.json()
         for livraison in liste_livraison:
             schema_livraison = LivraisonSchema()
             result_livraison = schema_livraison.load(livraison)  # deserialize the object
             #vérifier la si la livraison sera livré ou pas
             url = "http://127.0.0.1:5000/predict_livraison"

             payload = json.dumps({
                 "day": 1,
                 "month": 1,
                 "hub": 1,
                 "commune": 1,
                 "performance": 0.1
             })
             headers = {
                 'Content-Type': 'application/json'
             }

             response_prediction = requests.request("POST", url, headers=headers, data=payload)
             if (response_prediction==1):
                 print("hello")
             else:
                 print("coucou")
             #calculer le cumul R






         #construction de la liste JSON
         liste_rentabilite.append({
                "Id": 1,
                "Livreur": "Khalil Fadi",
                "Secteur": "Alger",
         })
     return jsonify(data=(liste_rentabilite,tournee_rentable,tournee_non_rentable)
        )