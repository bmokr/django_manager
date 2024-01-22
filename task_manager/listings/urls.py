from django.urls import path
from . import views
from .views import history_view


urlpatterns = [
    path('logged_home', views.logged_home, name='logged_home'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('<int:listing_id>/history/', history_view, name='history_view'),
    path('<int:listing_id>/history_view_acc/', views.history_view_acc, name='history_view_acc'),
    path('change_status', views.change_status, name='change_status'),
    path('<int:listing_id>/delete_listing', views.delete_listing, name='delete_listing'),
    path('add_new', views.add_new, name='add_new'),
    path('create_listing', views.create_listing, name='create_listing'),
]
