from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls import reverse

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dictionary = {
        "istanbul" : "30",
        "amsterdam" : "20",
        "paris" : [10,14,20,21],
        "rome" : {"morning" : 12, "evening" : 20},
        "user_premium" : False,
        "test" : "Test Test test Test"
        }
    return render(request, "template_app/weather.html",context=weather_dictionary)