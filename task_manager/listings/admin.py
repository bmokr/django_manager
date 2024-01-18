from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'status', 'list_date', 'show_history_link')
    list_display_links = ('id', 'title')
    list_filter = ('user', 'status')
    search_fields = ('id', 'title', 'user__username', 'status', 'description')
    list_per_page = 25

    def show_history_link(self, obj):
        return format_html('<a href="{}">History</a>', reverse('history_view', args=[obj.id]))

    show_history_link.short_description = 'History'
    show_history_link.allow_tags = True


admin.site.register(Listing, ListingAdmin)
