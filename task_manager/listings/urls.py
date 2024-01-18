from django.urls import path
from . import views
from .views import history_view


urlpatterns = [
    path('', views.index, name='logged_home'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('<int:listing_id>/history/', history_view, name='history_view'),
]
