from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .file_handler import *
from .validate_truck import *
truk_dict={}


@csrf_exempt
def load_question(request):
    if request.method=='POST':
        counter=int(request.POST['count'])
        if counter<len(questions):
            data = json.dumps({
            'counter': len(questions),
            'question': questions[counter],
            
    })
            return HttpResponse(data, content_type='application/json')
        else:
            return HttpResponse(json.dumps({'counter': len(questions),'question': "Your truck is registered successfully"}), content_type='application/json')



@csrf_exempt
def store(request):
   
    if request.method == 'POST':
        message=request.POST['message']
        counter=int(request.POST['count'])
        # if validate_input(message,counter):
        #     print("validated")
        # else:
        #     return HttpResponse('')
        if counter>=0 and counter<=len(fieldnames)-1:
            truk_dict[fieldnames[counter]]=message
            return HttpResponse('')
        else:
            dump_to_csv(truk_dict)
            return HttpResponse("done")

def home(request):
	return render(request,"chatbot/chat.html")