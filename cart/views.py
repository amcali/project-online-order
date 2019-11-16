from django.shortcuts import render, redirect, reverse
from .models import CartItem
from menu.models import Menu

# Create your views here.
def add_to_cart(request, product_id):
    
    #Identifies the product type being purchased
    product = Menu.objects.get(pk=product_id)
    
    #If product exists in the user's shopping cart
    existing_cart_item = CartItem.objects.get(owner=request.user, product=product)
    
    #If the item being added into the shopping cart does not exist, create a new one
    if existing_cart_item == None:
        new_cart_item = CartItem()
        new_cart_item.product = product
        new_cart_item.owner = request.user
        new_cart_item.quantity = 1
        new_cart_item.save()
    else:
        #Increase the product item quantity
        existing_cart_item.quantity += 1
        existing_cart_item.save()
    return redirect(reverse('menu'))
    

