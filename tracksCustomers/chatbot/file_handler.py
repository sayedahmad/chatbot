import csv
import os
from datetime import date

filename="truks.csv"


fieldnames = [
        'fleet_no', 
        'brand', 
        'type',
        'model',
        'engine_size',
        'no_of_wheels',
        'weight_kg',
        'customer'
        ]


questions=[
            'What is the fleet number of the vehicle',
            'What is the brand of the vehicle',
            'Please tell us the type of the vehicle.',
            'What is the model of the vehicle?',
            'please write the engine size of the vehicle.',
            'How many wheels does the vehicle have?',
            'Please type the vehicle weight in Kg',
            'Type the name of the fleet owner'
            ]


def dump_to_csv(truk_dict):
    with open(filename, mode='a+') as csv_file:
        fieldnames = ['fleet_no', 'brand', 'model','type','engine_size','no_of_wheels','weight_kg','customer','date']
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        if os.stat(filename).st_size == 0:
            writer.writeheader()
        truk_dict['date']=date.today()
        writer.writerow(truk_dict)

