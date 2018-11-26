from django.contrib import admin
from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.weather_list, name="weather_list"),
    path('create/', views.city_create, name="city_create"),
    path('<slug>/',views.weather_detail, name="weather_detail"),
    path('<slug>/delete/', views.city_delete, name="city_delete"),
    path('<slug>/edit/', views.city_edit, name='city_edit'),
]
