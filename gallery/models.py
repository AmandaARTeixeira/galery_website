from django.db import models
from datetime import datetime

class Photography(models.Model):
    OPCOES_CATEGORY = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ("PLANETA", 'Planeta')
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.CharField(max_length=100, choices=OPCOES_CATEGORY, default='')
    published = models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.name
