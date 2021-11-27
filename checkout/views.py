from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.context import cart_items

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('shopping_cart'))

    existsing_cart = cart_items(request)
    total = existsing_cart['grand_total']
    order_form = OrderForm()
    stripe_total = round(total * 100)
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, template, context)
