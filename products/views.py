from django.shortcuts import render
from .models import Product, Category

# Create your views here.

def all_categories(request):
    """ A view to categories """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    
    return render(request, 'products/categories.html', context)

def products(request):
    """
    Renders all products of same category
    """
    products = Product.objects.all()
    category_select = request.GET['category']

    if request.GET:
        if 'category' in request.GET:
            category_select = request.GET['category']
            products = products.filter(category__name=category_select)

    context = {
        'products': products,
        'current_category': category_select,
    }

    return render(request, 'products/products.html', context)
