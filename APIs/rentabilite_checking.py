import json
from datetime import date
from flask import jsonify
from  flask_restful import  Resource, request
import requests
import os,Data

from models.livraison_test import LivraisonTestSchema
from models.tournee_test import TourneeTestSchema


class calculRentabilite(Resource):

    def get(self):
     #initialisation
     liste_rentabilite=[]
     tournee_rentable=0
     tournee_non_rentable=0
     today=date.today()

     #Ramener la charge fixe
     charge_jour=150
     #Ramener les tournées pending
     with open('./Data/tournees.json', 'r') as file:
         data = file.read()
     tournees= json.loads(data)


     #Désialiser chaque tournée
     for tournee in tournees:
         rentabilite=0
         schema = TourneeTestSchema()
         result = schema.load(tournee)# deserialize the object
         id_tournee=result.idTournee


         #Ramener les livraisons de chaque tournée
         with open('./Data/livraisons.json', 'r',encoding='cp437') as file:
             data1 = file.read()
         livraisons=json.loads(data1)

         r=0
         #Désiarilser chaque livraison

         for livraison in livraisons:
             schema_livraison = LivraisonTestSchema()
             result_livraison = schema_livraison.load(livraison)  # deserialize the object

             if result_livraison.id_tournee== id_tournee:

                 url = "http://127.0.0.1:5000/predict_livraison"
                 payload = json.dumps({
                     "day": 20,
                     "month": 1,
                     "hub": int(result.hub),
                     "commune": int(result_livraison.commune),
                     "performance": float(result.performance)
                 })
                 headers = {
                     'Content-Type': 'application/json'
                 }
                 response_prediction = requests.request("POST", url, headers=headers, data=payload)

                 if response_prediction != 1:

                     r = r + ((result_livraison.prix_livraison_vendeur - (300 + charge_jour)) * 0.8)
                 else:
                     r = r + result_livraison.prix_livraison_vendeur - (300 + charge_jour)
                 # calculer le cumul R
             #vérifier si la livraison sera livré ou pas


         if (r>0):
             tournee_rentable=tournee_rentable+1
             #construction de la liste JSON
             liste_rentabilite.append({
                "Id": id_tournee,
                "Livreur": result.livreur,
                "Secteur": result.secteur,
                "Rentabilité":"Oui"
               })
         else:
             tournee_non_rentable=tournee_non_rentable+1
             liste_rentabilite.append({
                 "Id": id_tournee,
                 "Livreur": result.livreur,
                 "Secteur": result.secteur,
                 "Rentabilité": "Non"
             })
     response= jsonify(data=(liste_rentabilite,tournee_rentable,tournee_non_rentable))
     response.headers.add('Access-Control-Allow-Origin', '*')
     return response
