"""
This module returns the shopping cart page view
"""
from django.shortcuts import render


def shopping_cart(request):
    """ Returns shopping cart view"""
    return render(request, 'cart/shopping_cart.html')
