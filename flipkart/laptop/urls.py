from django.contrib import admin
from django.urls import path, include 
from .import views

urlpatterns = [
    path('Dell/',views.dell), 
    path('hp/',views.hp),
]
