"""
Provides URL path to the checkout page
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
