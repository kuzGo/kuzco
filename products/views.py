from django.shortcuts import render
from .models import Product

# Create your views here.


def all_watches(request):
    """ Shows all watches , handles sorting and searching """
    watches = Product.objects.all()

    context = {
        'watches': watches,
    }

    return render(request, 'watches/watches.html', context)
