"""
Provides URL path to reviews
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_total, name='reviews_total'),
    path('add/', views.add_reviews, name='add_reviews'),
    path('update/<int:review_id>/', views.update_reviews, name='update_reviews'),
    path('remove/<int:review_id>/', views.remove_review, name='remove_review'),
]
