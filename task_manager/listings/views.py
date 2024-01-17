from django.shortcuts import render
from .models import Listing


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings/logged_home.html', context)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
