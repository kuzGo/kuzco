"""
Provides URL path to reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_total, name='reviews_total'),
]
