from django.shortcuts import render, get_object_or_404, redirect
from apps.gallery.models import Photography
from django.contrib import messages
from apps.gallery.forms import PhotographyForms

def index(request):
    """
    View for the main gallery page.

    This view displays a list of published photography entries.
    If the user is not authenticated, they are redirected to the login page.

    Parameters:
    request: The HTTP request object.

    Returns:
    Rendered HTML template for the index page.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'No user logged in')
        return redirect('login')

    photography = Photography.objects.order_by('datetime').filter(published=True)

    return render(request, 'gallery/index.html', {'cards': photography})

def image(request, photography_id):
    """
    View for displaying a single photography.

    This view renders a specific photography based on the provided ID.
    If the photography is not found, it returns a 404 error.

    Parameters:
    request: The HTTP request object.
    photography_id: The ID of the photography to display.

    Returns:
    Rendered HTML template for the individual photography page.
    """
    photography = get_object_or_404(Photography, pk=photography_id)
    return render(request, 'gallery/image.html', {'photography': photography})

def search(request):
    """
    View for searching through photography entries.

    This view allows users to search for photography by name.
    If the user is not authenticated, they are redirected to the login page.
    The search results are filtered by published entries and the search query provided in the URL parameters.

    Parameters:
    request: The HTTP request object.

    Returns:
    Rendered HTML template for the search results page.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'No user logged in')
        return redirect('login')

    photographys = Photography.objects.order_by('datetime').filter(published=True)

    if 'search' in request.GET:
        searched_name = request.GET['search']
        if searched_name:
            photographys = photographys.filter(name__icontains=searched_name)

    return render(request, 'gallery/search.html', {'cards': photographys})

def add_image(request):
    """
    This view handles the addition of a new image. If the user is not authenticated,
    they will be redirected to the login page. If the form is submitted via a POST
    request and is valid, the image will be saved, and the user will be redirected to 
    the index page with a success message.
    """
    if not request.user.is_authenticated:
        messages.error(request, 'No user logged in')
        return redirect('login')

    form = PhotographyForms

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New phograpy added!')
            return redirect('index')


    return render(request, 'gallery/add_image.html', {'form': form})

def edit_image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)

    form = PhotographyForms(instance=photography)

    if request.method == 'POST':
        form = PhotographyForms(request.POST, request.FILES, instance=photography)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photography updated with success!')
            return redirect('index')

    return render(request, 'gallery/edit_image.html', {'form': form, 'photography_id' : photography_id})

def delete_image(request, photography_id):
    photography = get_object_or_404(Photography, pk=photography_id)

    photography.delete()

    messages.success(request, 'Image deleted with success!')

    return redirect('index')