"""
This module returns the shopping cart page view
"""
from django.shortcuts import render, redirect


def shopping_cart(request):
    """ Returns shopping cart view"""
    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """Adds a quantity of the items to the shopping cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
