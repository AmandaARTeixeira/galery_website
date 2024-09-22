from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Photography
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No user logged in')
        return redirect('login')

    photography = Photography.objects.order_by('datetime').filter(published=True)

    return render(request, 'gallery/index.html', {'cards' : photography})

def image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)
    return render(request, 'gallery/image.html', {'photography': photography})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No user logged in')
        return redirect('login')

    photographys = Photography.objects.order_by('datetime').filter(published=True)

    if 'search' in request.GET:
        searched_name = request.GET['search']
        if searched_name:
            photographys = photographys.filter(name__icontains=searched_name)
        
    return render(request, 'gallery/search.html', {'cards' : photographys})