import json


def validate_input(input_data, counter):
    if counter==0:
        if input_data.isdigit():
            return True
        else:
            return False
    else:
        print("other feild")
    # with open("truksSpecification.json") as json_file:
    #     truckspec=json.load(json_file)
    #     brandlist=list(truckspec["brand"].keys())
        
 


