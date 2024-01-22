from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .utils import process_history
from operator import itemgetter
from django.contrib.auth.models import User


def logged_home(request):
    listings = Listing.objects.order_by('-list_date')

    users = User.objects.all()

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    # User
    if 'user' in request.GET:
        user = request.GET['user']
        if user:
            listings = listings.filter(user__exact=user)

    # Status
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            listings = listings.filter(status__iexact=status)

    context = {
        'listings': listings,
        'users': users,
        'values': request.GET
    }
    return render(request, 'listings/logged_home.html', context)


def listing(request, listing_id):
    listing_s = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing_s,
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')


def history_view(request, listing_id):
    listing_s, new_table, user_table = process_history(request, listing_id)

    previous_page = '/admin/listings/listing/'

    context = {
        'listing': listing_s,
        'changes': new_table,
        'users': user_table,
        'previous_page': previous_page,
    }

    return render(request, 'admin/history_view.html', context)


def history_view_acc(request, listing_id):
    listing_s, new_table, user_table = process_history(request, listing_id)

    context = {
        'listing': listing_s,
        'changes': new_table,
        'users': user_table,
    }
    return render(request, 'listings/history_view_acc.html', context)


def change_status(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        status = request.POST['status_id']
        # user_id = request.POST['user_id']

        listing_s = Listing.objects.get(pk=listing_id)

        listing_s.status = status
        listing_s.save()

        return redirect('history_view_acc', listing_id=listing_id)


def delete_listing(request, listing_id):
    listing_s = get_object_or_404(Listing, pk=listing_id)
    listing_s.delete()
    return redirect('logged_home')


def add_new(request):
    users = User.objects.all()
    listing_s = Listing

    context = {
        'users': users,
        'listing': listing_s,
    }

    return render(request, 'listings/add_new.html', context)


def create_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        user_id = request.POST['user']

        Listing.objects.create(
            title=title,
            description=description,
            status=status,
            user_id=user_id
        )

        return redirect('logged_home')


def edit_listing_page(request, listing_id):
    users = User.objects.all()
    listing_s = get_object_or_404(Listing, pk=listing_id)

    context = {
        'users': users,
        'listing': listing_s,
    }
    return render(request, 'listings/edit_listing.html', context)


def edit(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        user_id = request.POST['user']

        listing_s = Listing.objects.get(pk=listing_id)
        listing_s.title = title
        listing_s.description = description
        listing_s.status = status
        listing_s.user_id = user_id
        listing_s.save()

        return redirect('history_view_acc', listing_id=listing_id)
