"""
Provides URL path to all watches 
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='watches'),
]
