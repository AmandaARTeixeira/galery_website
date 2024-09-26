from django.urls import path
from apps.gallery.views import index, image, search, add_image, edit_image, delete_image, filter

"""
URL configuration for the gallery app.

This module defines the URL patterns for the gallery application,
including the index page, individual photography view, and search functionality.
"""

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photography_id>/', image, name='image'),
    path('search/', search, name='search'),
    path('add-image/', add_image, name='add_image'),
    path('edit-image/<int:photography_id>/', edit_image, name='edit_image'),
    path('delete-image/<int:photography_id>/', delete_image, name='delete_image'),
    path('filter/<str:category>/', filter, name='filter'),
]