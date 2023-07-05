from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse

from django.contrib import messages

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
        messages.success(
            request,
            f'Changed quantity of {product.name} to {basket[item_id]}.')
        
    else:
        basket[item_id] = quantity
        messages.success(
            request, f'{product.name} successfully added to basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust quantity of basket items
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request,
            f'Changed quantity of {product.name} to {basket[item_id]}.')
        
    else:
        basket.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from basket.')

    request.session['basket'] = basket
    return redirect(reverse('basket'))

    


def remove_from_basket(request, item_id):
    """
    Remove items from shopping basket
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from basket.')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'There was an error while removing item: {e}')
        return HttpResponse(status=500)
