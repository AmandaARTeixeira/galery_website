"""
URL configuration for the setup project.

This module defines the URL patterns for the entire project, routing 
incoming requests to the appropriate views. It includes admin site URLs 
and app-specific URLs for the gallery and users applications.

For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views:
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views:
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for the project
urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URLs from the gallery application
    path('', include('apps.gallery.urls')),

    # Include URLs from the users application
    path('', include('apps.users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development

