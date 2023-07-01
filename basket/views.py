from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.

def view_basket(request):
    """ A view to a basket page """
    
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """
    allows items to be added to basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)