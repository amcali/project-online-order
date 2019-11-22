from django.urls import path, include
from .views import user_index, register, login, order_history, logout
from checkout.views import charge

urlpatterns = [
    path('', user_index, name='user_index'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('order_history', order_history, name='order_history'),
    path('register', register, name='user_register'),
    path("checkout/", include('checkout.urls'))
    
]
