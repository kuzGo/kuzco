from django.shortcuts import render, reverse, redirect

from django.contrib import messages
from django.conf import settings
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse('shopping_cart'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
