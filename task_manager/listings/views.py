from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .utils import pair_iterable_for_delta_changes
from operator import itemgetter

# from django.core.paginator import Paginator


def index(request):
    listings = Listing.objects.order_by('-list_date')

    # paginator = Paginator(listings, 6)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)

    context = {
        'listings': listings
    }
    return render(request, 'listings/logged_home.html', context)


def listing(request, listing_id):
    listing_s = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing_s
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')


def history_view(request, listing_id):
    listing_s = Listing.objects.get(pk=listing_id)
    history = listing_s.history.all().order_by('history_date').iterator()

    table = [('created', '-', '-')]
    for old_record, new_record in pair_iterable_for_delta_changes(history):
        delta = new_record.diff_against(old_record)
        inside_table = []
        for change in delta.changes:
            list_of_items = change.field, change.old, change.new
            inside_table.append(list_of_items)
        table.append(inside_table)

    history = listing_s.history.all().order_by('history_date').iterator()

    new_table = []
    user_table = []
    for item, entry in zip(table, history):
        if entry.history_user not in user_table:
            user_table.append(entry.history_user)

        new_item = (entry.id, entry.history_date, entry.history_user, entry.history_type,
                    item)
        new_table.append(new_item)

    sort_by = request.GET.get('sort_by', None)
    filter_user = request.GET.get('filter_user', None)

    if sort_by:
        if sort_by == 'history_date':
            new_table = sorted(new_table, key=itemgetter(1))
        elif sort_by == 'type':
            new_table = sorted(new_table, key=itemgetter(3))
        elif sort_by == 'history_user':
            new_table = sorted(new_table, key=lambda x: str(x[2]))
        else:
            new_table = sorted(new_table, key=itemgetter(0))

    if filter_user:
        new_table = [item for item in new_table if item[2].id == int(filter_user)]

    previous_page = '/admin/listings/listing/'

    context = {
        'listing': listing_s,
        'changes': new_table,
        'users': user_table,
        'previous_page': previous_page,
    }

    return render(request, 'admin/history_view.html', context)
