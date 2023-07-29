from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return index page """

    return render(request, 'home/index.html')


def about(request):
    """
    renders about page
    """
    return render(request, 'home/about.html')
