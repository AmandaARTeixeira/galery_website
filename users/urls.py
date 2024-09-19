from django.urls import path
from users.views import login, register, logout

urlpatterns = [
    path('', login, name='login'),
    path('', register, name='register'),
    path('', logout, name='logout')
]