from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls import reverse

def index(request):
    return render(request, "template_app/first.html")

