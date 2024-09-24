from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

"""
Models for the gallery application.

This module defines the Photography model, which represents a photography entry 
in the gallery, including its attributes such as name, caption, description, 
photo, category, publication status, date and time, and the user who posted it.
"""

class Photography(models.Model):
    """
    Model representing a photography entry.

    Attributes:
    - name: The name of the photography.
    - caption: A short caption for the photography.
    - description: A detailed description of the photography.
    - photo: The image file of the photography.
    - category: The category of the photography, chosen from predefined options.
    - published: Indicates if the photography should be published.
    - datetime: The date and time when the photography was created.
    - posted_by: The user who posted the photography, linked to the User model.
    """

    OPCOES_CATEGORY = [
        ('MIXED', 'Mixed'),
        ('MAINECOON', 'Maine Coon')
    ]

    name = models.CharField(max_length=100, null=False, blank=False)  # Photography name
    caption = models.CharField(max_length=150, null=False, blank=False)  # Short caption
    description = models.TextField(null=False, blank=False)  # Detailed description
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)  # Image upload path
    category = models.CharField(max_length=100, choices=OPCOES_CATEGORY, default='')  # Photography category
    published = models.BooleanField(default=False)  # Publication status
    datetime = models.DateTimeField(default=datetime.now, blank=False)  # Creation date and time
    posted_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name='user')  # User who posted

    def __str__(self) -> str:
        """Return the name of the photography as its string representation."""
        return self.name
