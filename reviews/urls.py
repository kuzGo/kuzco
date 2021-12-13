"""
Provides URL path to reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_reviews, name='add_reviews'),
]
