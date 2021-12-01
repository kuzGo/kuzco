"""
Provides URL path to the checkout page
"""
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('successful_checkout/<order_number>',
         views.successful_checkout, name='successful_checkout'),
    path('wh/', webhook, name='webhook'),     
]
