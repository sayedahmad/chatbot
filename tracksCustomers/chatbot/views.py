from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .file_handler import *
from .validate_truck import *
truk_dict={}


@csrf_exempt
def load_question(request):
    # the function loads questions
    # that are requested by the bot
    if request.method=='POST':
        counter=int(request.POST['count'])
        if counter<len(questions):
            data = json.dumps({
            'counter': len(questions),
            'question': questions[counter],
            
    })
            return HttpResponse(data, content_type='application/json')
        else:
            return HttpResponse(json.dumps({'counter': len(questions),'question': "Your truck is registered successfully press Enter to confirm"}), content_type='application/json')



@csrf_exempt
def store(request):
    # the function accepts post request for
    # storing and validating the input given by a customer
    if request.method == 'POST':
        message=request.POST['message']
        counter=int(request.POST['count'])
        if counter>=0 and counter<=len(fieldnames)-1:
            if not validate_input(message,counter):
                return HttpResponse("The input {} is not right. {}".format(message, error_messages[counter]))
            print("validation check complete")
        
            truk_dict[fieldnames[counter]]=message
            return HttpResponse('')
        else:
            print("we are saving the dict")
            dump_to_csv(truk_dict)
            return HttpResponse('Thank you for the participation')

def home(request):
    # the method loads the chatbot template
	return render(request,"chatbot/chat.html")