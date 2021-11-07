from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_watches(request):
    """ Shows all watches , handles sorting and searching """
    watches = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            watches = watches.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, 'Please enter any search criteria.')
                return redirect(reverse('watches'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            watches = watches.filter(queries)
    context = {
        'watches': watches,
        'search_term': query,
        'categories': categories,
    }

    return render(request, 'watches/watches.html', context)


def watch_details(request, product_id):
    """ Shows details of idividual watch """
    watch_detail = get_object_or_404(Product, pk=product_id)

    context = {
        'watch_detail': watch_detail,
    }

    return render(request, 'watches/watches_description.html', context)
