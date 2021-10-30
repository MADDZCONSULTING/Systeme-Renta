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

     #Ramener la charge fixe
     charge_jour=100
     #Ramener les tournées pending
     url = "https://dev.easy-relay.com/api/mob2/api.php?action=getTourneeDay&"+"day=2021-02-10"+"&etat=3&type=l"
     payload = {}
     headers = {
         'email': 'dm@er.com',
         'mdp': 'test'
     }
     response = requests.request("GET", url, headers=headers, data=payload)
     tournees= response.json()
     print(tournees)

     #Désialiser chaque tournée
     for tournee in tournees:
         rentabilite=0
         schema = TourneeSchema()
         result = schema.load(tournee)# deserialize the object
         id_tournee=result.idTournee
         #Ramener les livraisons de chaque tournée
         url = "https://dev.easy-relay.com/api/mob2/api.php?action=getLvTournee&id_tournee="+id_tournee
         payload = {}
         headers = {
             'email': 'dm@er.com',
             'mdp': 'test'
         }
         response_livraisons = requests.request("GET", url, headers=headers, data=payload)
         liste_livraison=response_livraisons.json()
         r=0
         #Désiarilser chaque livraison
         for livraison in liste_livraison:
             schema_livraison = LivraisonSchema()
             result_livraison = schema_livraison.load(livraison)  # deserialize the object
             #vérifier si la livraison sera livré ou pas
             url = "http://127.0.0.1:5000/predict_livraison"
             payload = json.dumps({
                 "day": 10,
                 "month": 2,
                 "hub": result.hub,
                 "commune": result_livraison.commune_client,
                 "performance": 0.8
             })
             headers = {
                 'Content-Type': 'application/json'
             }
             response_prediction = requests.request("POST", url, headers=headers, data=payload)

             if response_prediction != 1:
                #print(type(result_livraison.prix_livraison))
                #print(type(charge_jour))
                r = r +( (result_livraison.prix_livraison - (200 + charge_jour)) * 0.8)
             else:
                r= r + result_livraison.prix_livraison - (200 + charge_jour)
             #calculer le cumul R

         if (r>0):
             tournee_rentable=tournee_rentable+1
             #construction de la liste JSON
             liste_rentabilite.append({
                "Id": id_tournee,
                "Livreur": "Khalil Fadi",
                "Secteur": "Alger",
                "Rentabilité":"Oui"
               })
         else:
             tournee_non_rentable=tournee_non_rentable+1
             liste_rentabilite.append({
                 "Id": id_tournee,
                 "Livreur": "Khalil Fadi",
                 "Secteur": "Alger",
                 "Rentabilité": "Non"
             })

     return jsonify(data=(liste_rentabilite,tournee_rentable,tournee_non_rentable)
        )