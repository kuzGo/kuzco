"""
Provides URL path to all watches
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='watches'),
    path('<product_id>', views.watch_details, name='watch_detail'),
    path('add/', views.add_watch, name='add_watch'),
]
