from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.http import JsonResponse
import keyboard
import time
# Create your views here.
@api_view(['GET'])
def index(request):
    return Response("Hello, World!")

@csrf_exempt
@api_view(['POST'])
def on_message(request):
    msg = request.data
    # print(msg)
    user_number, user_name = msg.get("From").split(":")[1], msg.get("ProfileName")
    text = msg.get("Body").lower()
    words = text.split(" ")
    media_url = None
    if user_number=='+916303496380' or user_number=='+919494022833':
        time.sleep(0)
        print(text)
        # for i in text:
        #     time.sleep(0)
        #     keyboard.write(i)
        

    return JsonResponse({'status': 'success','text':text}, status=200)