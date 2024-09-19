from django.shortcuts import render
from users.forms import LoginForm, RegisterForm

def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    return render(request, 'users/logout.html')
