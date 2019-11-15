from django.urls import path
from .views import index, register, login, profile, logout

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='user_profile'),
    path('register', register, name='user_register')
]
