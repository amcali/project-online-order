from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .models import CartItem
from menu.models import Menu

# Create your views here.


"""View products ordered """
def view_cart(request):
    #request:user is user that is currently logged in
    all_cart_items = CartItem.objects.filter(owner=request.user)

    return render(request, 'cart/view_cart.template.html', {
        'all_cart_items': all_cart_items,
    })

    
""" Add product to cart function """
def add_to_cart(request, product_id):
    

    #Identifies the product type being purchased
    product = Menu.objects.get(pk=product_id)
    
    #If product exists in the user's shopping cart
    existing_cart_item = CartItem.objects.filter(owner=request.user, product=product).first()
    
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


""" Reduce product quantity in cart function """
def reduce_from_cart(request, product_id):
    
    #Identifies the product type being purchased
    product = Menu.objects.get(pk=product_id)
    
    #If product exists in the user's shopping cart
    existing_cart_item = CartItem.objects.filter(owner=request.user, product=product).first()
    
    #If the item being added into the shopping cart exists, reduce from it
    if existing_cart_item == None:
        pass
    elif existing_cart_item.quantity > 1:
        existing_cart_item.quantity -= 1
        existing_cart_item.save()
    elif existing_cart_item.quantity == 1:
        #If the product is already 0, and user continues to reduce, then item will be removed from the cart
        existing_cart_item.delete()
    return redirect(reverse('menu'))
    

""" Clear by product type from cart function """
def clear_from_cart(request, cart_item_id):
    
    existing_cart_item = CartItem.objects.get(pk=cart_item_id)
    existing_cart_item.delete()
    return redirect(reverse('view_cart'))