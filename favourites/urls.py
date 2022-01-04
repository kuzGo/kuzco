"""
Provides URL path to the favourites
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_favourites, name='all_favourites'),
    path('add/<int:product_id>/', views.add_favourites, name='add_favourites'),
    path('delete/<int:product_id>/',
         views.delete_favourites, name='delete_favourites'),
]
