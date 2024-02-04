from django.urls import path
from . import views

app_name = "template_app" #app name register. {% app_name:view %}

urlpatterns = [
    path("", views.index, name="index"),
    path("weather/", views.weather_view, name="weatherview")

]