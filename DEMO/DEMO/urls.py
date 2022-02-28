from django.contrib import admin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import path
from fine.models import Car, Fine
import json

answers = {
    1: {
        'name plate': 'MH 02 BY 3964',
        'speed': 117,
        'image url': '/static/result/1.jpg',
        'fine': 4500
    },
    2: {
        'name plate': 'MH 02 BY 3964',
        'speed': 42,
        'image url': '/static/result/2.jpg',
        'fine': 0
    },
    3: {
        'name plate': 'MH 02 FJ 6139',
        'speed': 52,
        'image url': '/static/result/3.jpg',
        'fine': 4500
    },
    4: {
        'name plate': 'MH 04 GE 4307',
        'speed': 70,
        'image url': '/static/result/4.jpg',
        'fine': 4500
    },
}

def demo_view(request: HttpRequest):
    if request.method == 'GET': return render(request, 'demo.html')

    data = request.body
    content = json.loads(data)

    if 'type' in content:
        print('->',content)  
        name_plate = content['data']['name plate']
        car = Car.objects.filter(license_plate=name_plate).first()
        fine = Fine()
     
        fine.amount = content['data']['fine']
        fine.comment = content['data']['comment']
        fine.speed = content['data']['speed']
        fine.car = car
        fine.save()
        
        
        return JsonResponse({ 'comment' : 'recieved' })

    data = answers[int(content['selected'])]

    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', demo_view),
]
