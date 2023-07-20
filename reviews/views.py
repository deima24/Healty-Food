from django.shortcuts import render

def entry_list(request):
    context = {}

    return render(request, 'reviews/review.html', context)