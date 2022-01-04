"""
A view to display a list of favourite items,
adding and removing items from the list
"""

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Favourites


@login_required
def all_favourites(request):
    """
    A view displaying all favourite items
    for the user
    """
    favourite = None
    try:
        favourite = Favourites.objects.get(user=request.user)
    except Favourites.DoesNotExist:
        pass

    context = {
        'favourite': favourite,
    }

    return render(request, 'favourites/favourites.html', context)


@login_required
def add_favourites(request, product_id):
    """
    A view to add an item to a list of
    favourite items
    """
    watch = get_object_or_404(Product, pk=product_id)
    favourite, _ = Favourites.objects.get_or_create(user=request.user)
    favourite.watches.add(watch)
    messages.info(request, "A new item was added to your favourites")
    return redirect(reverse('all_favourites'))


@login_required
def delete_favourites(request, product_id):
    """
    A view to remove an item from a list of
    favourite items
    """
    favorite_item = Favourites.objects.get(user=request.user)
    watch_card = get_object_or_404(Product, pk=product_id)
    favorite_item.watches.remove(watch_card)
    messages.info(
        request, f'{watch_card.name} was removed from your favourites')
    return redirect(reverse('all_favourites'))
