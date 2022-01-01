"""
Provides URL path to all watches
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_watches, name='watches'),
    path('<product_id>', views.watch_details, name='watch_detail'),
    path('add/', views.add_watch, name='add_watch'),
    path('update/<int:product_id>/',
         views.update_watches,
         name='update_watches'),
    path('remove/<int:product_id>/',
         views.remove_watches,
         name='remove_watches'),
]
