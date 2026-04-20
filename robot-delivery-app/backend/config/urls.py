# """Root URL Configuration"""
# from django.contrib import admin
from django.urls import path
from . import views

api_v1 = [
    path('config/', views.config, name='config'),
]


