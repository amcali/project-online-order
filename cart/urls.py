
from django.urls import path, include
from .views import add_to_cart, view_cart, clear_from_cart, reduce_from_cart

urlpatterns = [
    path('view', view_cart, name='view_cart'),
    path('add_to_cart/<product_id>', add_to_cart, name='add_to_cart'),    
    path('reduce_from_cart/<product_id>', reduce_from_cart, name="reduce_from_cart"),
    path('clear_from_cart/<cart_item_id>', clear_from_cart, name='clear_from_cart')
]
