from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm

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

def product_detail(request, product_id):
    """
    Displays product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)



def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorised to do this!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product was added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)