
# it also holds lists of questions and error messages

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


error_messages=[
    '<span style="color:red">Type the fleet number in digit</span>',
    '<span style="color:red"> Type a well known brand like MAN, Volvo</span>',
    '<span style="color:red">Write the truck type like petrol, diesel</span>',
    '<span style="color:red">please type the correct model for a brand such as MAN TGX EVOLION for brand MAN</span>',
    '<span style="color:red">Type the engin size in letters like 2,4,8</span>',
    '<span style="color:red">please input the number of wheels in digit</span>',
    '<span style="color:red">please rewrite the weight in Kg only digits needed</span>',
    '<span style="color:red">please write the name of the customer only letters required</span>'
]

questions=[
            'What is the fleet number of the truck?',
            'What is the brand of the truck?',
            'Please tell us the type of the truck (petrol, diesel or gas).',
            'What is the model of the truck?',
            'please write the engine size of the truck in litters (only in digit)',
            'How many wheels does the truck have? (only in digit)',
            'Please type the vehicle weight in Kg (only in digit)',
            'What is the name of the fleet owner?'
            ]


def dump_to_csv(truk_dict):
    # The function stores the chat data to trucks.csv file
    with open(filename, mode='a+') as csv_file:
        fieldnames = ['fleet_no', 'brand', 'model','type','engine_size','no_of_wheels','weight_kg','customer','date']
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        if os.stat(filename).st_size == 0:
            writer.writeheader()
        truk_dict['date']=date.today()
        writer.writerow(truk_dict)

