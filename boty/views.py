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
'''
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
        

    return JsonResponse({'status': 'success','text':text}, status=200)'''
'''@csrf_exempt
@api_view(['GET', 'POST'])
def on_message(request):
    if request.method == 'POST':
        msg = request.data
        user_number, user_name = msg.get("From").split(":")[1], msg.get("ProfileName")
        text = msg.get("Body").lower()
        print(text)

        # keyboard.write(text)  # Optional: uncomment if needed

        return JsonResponse({'status': 'success', 'text': text}, status=200)

    # Optional: For GET requests (e.g., browser test)
    return JsonResponse({'status': 'GET received - use POST to send message'}, status=200)
'''
# global message store
latest_message = {"text": "", "timestamp": None}

@csrf_exempt
@api_view(['GET', 'POST'])
def on_message(request):
    global latest_message

    if request.method == 'POST':
        msg = request.data
        user_number = msg.get("From", "").split(":")[1]
        text = msg.get("Body", "")

        if user_number in ['+916303496380', '+918099340432']:
            print(text)
            latest_message["text"] = text
            latest_message["timestamp"] = time.time()

        return JsonResponse({'status': 'success', 'text': text}, status=200)

    elif request.method == 'GET':
        return JsonResponse({'text': latest_message["text"]}, status=200)
