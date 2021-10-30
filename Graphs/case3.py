
import json

def case3():
    with open('./Data/simulation3.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/simulation.json', 'w') as f:
        json.dump(new_data, f)
    with open('./Data/tournee3.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/tournees.json', 'w') as f:
        json.dump(new_data, f)
    with open('./Data/livraison3.json', 'r', encoding='cp437') as file:
        data = file.read()
        new_data = json.loads(data)
        print(new_data)
    with open('./Data/livraisons.json', 'w') as f:
        json.dump(new_data, f)
