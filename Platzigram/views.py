"""
Views de platzi
"""
from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))

