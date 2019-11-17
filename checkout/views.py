from django.shortcuts import render, HttpResponse
from cart.models import CartItem
from .forms import OrderForm, PaymentForm
from django.conf import settings
import stripe

# Create your views here.

""" Function to calculate the total cost of all items in user's cart """
def calculate_cart_cost(request):
    all_cart_items = CartItem.objects.filter(owner=request.user)
    amount = 0
    for cart_item in all_cart_items:
        amount += cart_item.product.cost * cart_item.quantity
    return amount

""" Renders total amount user needs to pay for items in cart """
def checkout(request):

    total_cost = calculate_cart_cost(request)

    return render(request, 'checkout/checkout.template.html', {
        'total_cost': total_cost/100
    })

""" Renders page for checkout details of items to pay for """
def charge(request):
    
    amount = calculate_cart_cost(request)
    
    if request.method == "GET":
        
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'checkout/charge.template.html', {
            'order_form': order_form,
            'payment_form': payment_form,
            'amount': amount,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        stripeToken = request.POST['stripe_id']
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            customer = stripe.Charge.create(
                amount = int(request.POST['amount']),
                currency = 'sgd',
                description = 'Payment',
                card = stripeToken
                )
            if customer.paid:
                return HttpResponse("Payment successful")
            else:
                return HttpResponse("Payment has failed")
        return HttpResponse(stripeToken)