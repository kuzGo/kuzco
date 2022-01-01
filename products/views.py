from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_watches(request):
    """ Shows all watches , handles sorting and searching """
    watches = Product.objects.all().order_by('id')
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'name':
                sorting = 'lower_name'
                watches = watches.annotate(lower_name=Lower('name'))
            if sorting == 'category':
                sorting = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sorting = f'-{sorting}'
            watches = watches.order_by(sorting)

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

    current_sorting = f'{sort}_{direction}'

    watches_paginator = Paginator(watches, 8)

    page_num = request.GET.get('page')

    page = watches_paginator.get_page(page_num)
    context = {
        'page': page,
        'search_term': query,
        'categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'watches/watches.html', context)


def watch_details(request, product_id):
    """ Shows details of idividual watch """
    watch_detail = get_object_or_404(Product, pk=product_id)

    context = {
        'watch_detail': watch_detail,
    }

    return render(request, 'watches/watches_description.html', context)


@login_required
def add_watch(request):
    """ Add watches to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, you do not have permission\
             to perform these actions.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, "Successfully added a watch to the store")
            return redirect(reverse('watch_detail', args=[product.id]))
        else:
            messages.error(
                request, "Failed to add a watch.\
                    Please ensure the form is valid")
    else:
        form = ProductForm()
    template = 'watches/add_watches.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_watches(request, product_id):
    """ Updates existing watch """
    if not request.user.is_superuser:
        messages.error(request,  "Sorry, you do not have permission\
             to perform these actions.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product.")
            return redirect(reverse('watch_detail', args=[product.id]))
        else:
            messages.error(
                request, "Failed to update this product. \
                    Please ensure the form is valid.")
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'watches/update_watches.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def remove_watches(request, product_id):
    """Delete a watch/product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('home'))

    watches = get_object_or_404(Product, pk=product_id)
    watches.delete()
    messages.success(request, f'{watches.name} has been succeffuly deleted.')
    return redirect(reverse('watches'))
