from django.contrib import admin
from .models import CartItem

# Register your models here.
# This is the model for the shopping cart
admin.site.register(CartItem)