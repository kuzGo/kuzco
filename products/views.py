from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_watches(request):
    """ Shows all watches , handles sorting and searching """
    watches = Product.objects.all()

    context = {
        'watches': watches,
    }

    return render(request, 'watches/watches.html', context)


def watch_details(request, product_id):
    """ Shows details of idividual watch """
    watch_detail = get_object_or_404(Product, pk=product_id)

    context = {
        'watch_detail': watch_detail,
    }

    return render(request, 'watches/watches_description.html', context)
