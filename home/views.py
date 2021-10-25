"""
This module returns the home page view
"""
from django.shortcuts import render


def index(request):
    """ Returns index page view"""
    return render(request, 'home/index.html')
