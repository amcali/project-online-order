from django.shortcuts import render
from cart.models import CartItem

# Create your views here.

def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.product.cost * cart_item.quantity
    return amount

def checkout(request):

    total_cost = calculate_cart_cost(request)

    return render(request, 'checkout/checkout.template.html', {
        'total_cost': total_cost/100
    })
