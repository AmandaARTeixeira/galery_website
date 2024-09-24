from django.urls import path
from apps.users.views import login, register, logout

"""
URL configuration for user authentication.

This module defines the URL patterns for user-related views,
including login, registration, and logout functionalities.
"""

urlpatterns = [
    # URL pattern for the login page. Maps to the login view.
    path('login/', login, name='login'),

    # URL pattern for the registration page. Maps to the register view.
    path('register/', register, name='register'),

    # URL pattern for user logout. Maps to the logout view.
    path('logout/', logout, name='logout'),
]