
import json



def validate_input(input_data, counter):
    # this funcition validates the given input for each question 
    # if the input is invalid the bot will reject it.
    if counter==0:
        if input_data.isdigit():
            return True
        else:
            return False
    elif counter==1:
        if input_data.lower() in pars_json_file("brand"):
            return True
        else:
            return False
    elif counter==2:
        if input_data.lower() in pars_json_file("type"):
            return True
        else:
            return False

    elif counter==3:
        if any(input_data in models for models in pars_json_file("model")):
            return True
        else:
            return False
    elif counter==4 or counter==5 or counter==6:
        if input_data.isdigit():
            return True
        else:
            return False
    
    elif counter==7:
        if not input_data.isdigit():
            return True
        else:
            return False
    else:
        print("other feild")
    
    
    
    
def pars_json_file(data_type):
    # this function read a json file where all the brands, model and types are stored
    filename="trucks_spec.json"    
    with open(filename) as json_file:
        truckspec=json.load(json_file)
        if data_type=="brand":
            return list(truckspec["brand"].keys())
        elif data_type=="type":
            return list(truckspec["type"])
        elif data_type=="model":
            return [truckspec["brand"][model] for model in list(truckspec["brand"].keys())]
        
 


