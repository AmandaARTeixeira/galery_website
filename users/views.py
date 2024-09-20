from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            usr_name = form['name_login'].value()
            usr_password = form['password'].value()
            
            user = auth.authenticate(
                request,
                username=usr_name,
                password=usr_password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, f'{usr_name} successfully logged in')
                return redirect('index')
            else:
                messages.error(request, 'User and/or password incorrect')
                return redirect('login')
        
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'Passwords are not the same')
                return redirect('register')
                
            usr_name = form['name_register'].value()
            usr_email = form['email'].value()
            usr_password = form['password1'].value()

            if User.objects.filter(username=usr_name).exists():
                messages.error('This username is not availiable')
                return redirect('register')
            
            User.objects.create_user(
                username=usr_name,
                email=usr_email,
                password=usr_password
            )

            messages.success(request, 'User registered with success')
            return redirect('login')
            

    return render(request, 'users/register.html', {'form': form})

def logout(request):
    return render(request, 'users/logout.html')
