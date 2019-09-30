from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from .chatbot import *


# Train based on the english corpus

#Already trained and it's supposed to be persistent
# chatbot.train("chatterbot.corpus.english")

@csrf_exempt
def get_response(request):
    response = {'status': None}
    if request.method == 'POST':
        message=request.POST['message']
        chat_response = chatbot.get_response(message).text
		# response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		# response['status'] = 'ok'
        return HttpResponse(chat_response)
    # else:
    #     return HttpResponse('no response')



def home(request):
	return render(request,"chatbot/chat.html")