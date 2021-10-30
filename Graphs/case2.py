from flask import jsonify
from  flask_restful import  Resource, request
from apscheduler.schedulers.background import BackgroundScheduler
import json

def case2():
    with open('./Data/simulation2.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/simulation.json', 'w') as f:
        json.dump(new_data, f)

    with open('./Data/tournee2.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/tournees.json', 'w') as f:
        json.dump(new_data, f)
    with open('./Data/livraison2.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/livraisons.json', 'w') as f:
        json.dump(new_data, f)



