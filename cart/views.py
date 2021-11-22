"""
This module returns the shopping cart page view
"""
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def shopping_cart(request):
    """ Returns shopping cart view"""
    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, item_id):
    """Adds a quantity of the items to the shopping cart"""
    product = Product.objects.get(pk=item_id)
    message = f'Successfully added { product. name} to your cart'
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, message)

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        del cart[item_id]
    request.session['cart'] = cart
    return redirect(reverse('shopping_cart'))


def delete_item(request, item_id):
    try:
        cart = request.session.get('cart', {})
        del cart[item_id]
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
