from django.shortcuts import render, get_object_or_404
from gallery.models import Photography

def index(request):    
    photography = Photography.objects.all()

    return render(request, 'gallery/index.html', {'cards' : photography})

def image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)
    return render(request, 'gallery/image.html', {'photography': photography})
