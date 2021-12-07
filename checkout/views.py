import json
from django.shortcuts import (
    render, reverse, redirect, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe

from cart.context import cart_items

from products.models import Product
from .models import Order, OrderLineItem
from .forms import OrderForm


@require_POST
def saved_info_checkout(request):
    try:
        payment_intent_id = request.POST.get(
            'client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, 'We are unable to process your  \
            card at the moment. Please try again later.')
        return HttpResponse(content=error, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county']
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            payment_intent_id = request.POST.get(
                'client_secret').split('_secret')[0]
            order.stripe_pay_id = payment_intent_id
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "We couldn't find one of the products in our database"
                        "Please contact our customer support for help."
                    ))
                    order.delete()
                    return redirect(reverse, ('shopping_cart'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('successful_checkout', args=[order.order_number]))
        else:
            messages.error(request, (
                'An error occured with your form'
                'Ensure you entered valid information.'
            ))

    else:
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
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def successful_checkout(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order {order_number} has been succefully completed \
        We sent an email to {order.email} address.')
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/successful_checkout.html'

    context = {
        'order': order,
    }
    return render(request, template, context)
