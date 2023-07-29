from django.shortcuts import render


def handler404(request, exception):
    """ Costumized 404 Page """
    return render(request, "errors/404.html", status=404)
