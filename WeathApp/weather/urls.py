from django.contrib import admin
from django.urls import path, include
from weather import views
from weather.views import save_weather_details


urlpatterns = [
    path('', views.index),
    path('delete-city/', views.delete_city, name='delete_city'),
    path('save-weather-details/', save_weather_details, name='save_weather_details'),
]