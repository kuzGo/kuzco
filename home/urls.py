"""
Provides URL path to the home page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
