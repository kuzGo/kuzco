from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from cart.context import cart_items
from .forms import OrderForm
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
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'client_secret': intent.client_secret,
        'stripe_public_key': stripe_public_key,
    }
    return render(request, template, context)
