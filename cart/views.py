"""
This module returns the shopping cart page view
"""
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def shopping_cart(request):
    """ Returns shopping cart view"""
    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """Adds a quantity of the items to the shopping cart"""
    product = get_object_or_404(Product, pk=item_id)
    message = f'Successfully added { product. name} to your cart'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Successfully updated \
                { product. name} to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, message)

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """Modifies the items of the shopping cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Successfully updated \
                { product. name} to {cart[item_id]}')
    else:
        del cart[item_id]
        messages.success(request, f'Successfully removed \
            { product. name} from your shopping cart')
    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def delete_item(request, item_id):
    """Removes the items from the shopping cart"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        del cart[item_id]
        messages.success(request, f'Successfully removed \
            { product. name} from your shopping cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(
            request, f'Error {error} occured removing \
            item from your shopping cart')
        return HttpResponse(status=500)
