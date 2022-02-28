from django.contrib import admin
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.urls import path

import json

answers = {
    1: {
        'name plate': 'MH 02 CX 1412',
        'speed': 40,
        'image url': '/static/result/1.jpg',
        'fine': 4500
    },
    2: {
        'name plate': 'MH 02 AC 5555',
        'speed': 110,
        'image url': '/static/result/1.jpg',
        'fine': 4500
    },
    3: {
        'name plate': 'MH 01 XX 831',
        'speed': 55,
        'image url': '/static/result/1.jpg',
        'fine': 4500
    },
    4: {
        'name plate': 'MH 01 CA 3453',
        'speed': 30,
        'image url': '/static/result/1.jpg',
        'fine': 4500
    },
}

def demo_view(request: HttpRequest):
    if request.method == 'GET': return render(request, 'demo.html')

    data = request.body
    content = json.loads(data)
    data = answers[int(content['selected'])]

    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', demo_view),
]
