from django.contrib import admin
from gallery.models import Photography

class ListingPhotographys(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)
    list_per_page = 10
    list_editable = ('published',)

admin.site.register(Photography, ListingPhotographys)
