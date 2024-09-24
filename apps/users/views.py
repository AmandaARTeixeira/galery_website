from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

"""
Views for user authentication in the application.

This module defines views for user login, registration, and logout,
handling form submissions and user authentication.
"""

def login(request):
    """
    View for user login.

    This view handles the login process by validating user credentials
    through a form. If the credentials are correct, the user is logged in
    and redirected to the index page. If the credentials are incorrect,
    an error message is displayed.

    Parameters:
    request: The HTTP request object.

    Returns:
    Rendered HTML template for the login page or redirects on success.
    """
    form = LoginForm()  # Initialize the login form
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Bind data to the form

        if form.is_valid():  # Validate the form
            usr_name = form['name_login'].value()  # Get username from form
            usr_password = form['password'].value()  # Get password from form
            
            # Authenticate the user
            user = auth.authenticate(
                request,
                username=usr_name,
                password=usr_password
            )

            if user is not None:  # User found
                auth.login(request, user)  # Log in the user
                messages.success(request, f'{usr_name} successfully logged in')  # Success message
                return redirect('index')  # Redirect to the index page
            else:  # Authentication failed
                messages.error(request, 'User and/or password incorrect')  # Error message
                return redirect('login')  # Redirect back to login

    return render(request, 'users/login.html', {'form': form})  # Render the login template

def register(request):
    """
    View for user registration.

    This view handles user registration by processing the registration
    form. If the registration is successful, the user is created and
    redirected to the login page. If the username is already taken,
    an error message is displayed.

    Parameters:
    request: The HTTP request object.

    Returns:
    Rendered HTML template for the registration page or redirects on success.
    """
    form = RegisterForm()  # Initialize the registration form

    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Bind data to the form
        
        if form.is_valid():  # Validate the form                
            usr_name = form['name_register'].value()  # Get username from form
            usr_email = form['email'].value()  # Get email from form
            usr_password = form['password1'].value()  # Get password from form

            # Check if the username is already taken
            if User.objects.filter(username=usr_name).exists():
                messages.error(request, 'This username is not available')  # Error message
                return redirect('register')  # Redirect back to registration
            
            # Create a new user
            User.objects.create_user(
                username=usr_name,
                email=usr_email,
                password=usr_password
            )

            messages.success(request, 'User registered successfully')  # Success message
            return redirect('login')  # Redirect to login page

    return render(request, 'users/register.html', {'form': form})  # Render the registration template

def logout(request):
    """
    View for user logout.

    This view handles the logout process by logging the user out
    and redirecting them to the login page with a success message.

    Parameters:
    request: The HTTP request object.

    Returns:
    Redirects to the login page after logging out.
    """
    auth.logout(request)  # Log out the user
    messages.success(request, 'User successfully logged out')  # Success message
    return redirect('login')  # Redirect to the login page
