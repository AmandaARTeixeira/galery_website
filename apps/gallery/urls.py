from django.urls import path
from apps.gallery.views import index, image, search

"""
URL configuration for the gallery app.

This module defines the URL patterns for the gallery application,
including the index page, individual photography view, and search functionality.
"""

urlpatterns = [
    # URL pattern for the index page. Maps to the index view.
    path('', index, name='index'),

    # URL pattern for viewing a specific photography.
    # The photography_id parameter is captured from the URL as an integer.
    path('image/<int:photography_id>/', image, name='image'),

    # URL pattern for the search page. Maps to the search view.
    path('search/', search, name='search'),
]