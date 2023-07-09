from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.

def checkout(request):
    basket = request.session.get('basket',{})
    if not basket:
        messages.error(request, "Your basket is currently empty.")
        return redirect(reverse('categories'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NS5qfEcKFRGV4ZzCXs6oHUl3GW74pBAoqv3tEApwrXrMETbZtgapXBzR6NiTggEVZIKdlCNy9IefLpWqdpWAQzT00SxHbF0yx',
        'stripe_secret_key': 'sk_test_51NS5qfEcKFRGV4ZzSPm3vETAF6uSAyOOAaeB3139RY7Koz5I7AG7akFagCtKRgqmlZJzEGDS5p5cfztXDbSSLDOh00Gtj08EXT'
    }

    return render(request, template, context)