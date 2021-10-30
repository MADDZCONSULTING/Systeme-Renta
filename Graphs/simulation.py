
from flask import jsonify
from  flask_restful import  Resource, request
from apscheduler.schedulers.background import BackgroundScheduler
import json
from models.variable import VariableGlobaleSchema
from Graphs.case1 import case1
from Graphs.case2 import case2
from Graphs.case3 import case3

class Simulation(Resource):

    def get(self):
     #ouvrir le fichier
     with open('./Data/variable.json', 'r', encoding='cp437') as file:
         variable = file.read()
         variable_to_read=json.loads(variable)
         var = VariableGlobaleSchema()
         print(variable)
         result = var.load(variable_to_read)  # deserialize the object
         print(result.cpt)
         if(result.cpt==1):
             print(1)
             case1()
         if(result.cpt==2):
             print(2)
             case2()
         if (result.cpt == 3):
             print(3)
             case3()


         result.cpt=result.cpt+1
         save=var.dump(result)
     with open('./Data/variable.json', 'w') as f:
             json.dump(save, f)

     cpt=1
     #confirmer que l'api marche
     response = jsonify(data=(cpt))
     response.headers.add('Access-Control-Allow-Origin', '*')
     return response
