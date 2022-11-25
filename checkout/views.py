

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# test key pk_test_51M84AgAYOJ9b3UAu2CsHcVDTHR4qOAzv6UxJWlY4NdhgYCNLWgbESeyF5ClxdIdrCSGwx4FDOEZD6JkZUxt8VJ6s00EMnRW9vV
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M84AgAYOJ9b3UAu2CsHcVDTHR4qOAzv6UxJWlY4NdhgYCNLWgbESeyF5ClxdIdrCSGwx4FDOEZD6JkZUxt8VJ6s00EMnRW9vV',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)