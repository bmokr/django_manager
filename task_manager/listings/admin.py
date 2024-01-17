from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('user', 'status')
    search_fields = ('id', 'title', 'user__username', 'status', 'description')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
