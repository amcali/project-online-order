from django.shortcuts import render, HttpResponse
from cart.models import CartItem
from .forms import OrderForm, PaymentForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from .models import Charge, Transaction, LineItem

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
        
        #@todo: to prevent the same transaction being created again
        transaction = Transaction()
        transaction.owner = request.user
        # transaction.cart_items = CartItem.objects.filter(owner=request.user)
        transaction.status = "pending"
        transaction.date = timezone.now()
        transaction.save()
        
        all_cart_items = CartItem.objects.filter(owner=request.user)
        for cart_item in all_cart_items:
            lineItem = LineItem()
            lineItem.transaction = transaction
            lineItem.product = cart_item.product
            lineItem.name = cart_item.product.name
            lineItem.sku = cart_item.product.sku
            lineItem.cost = cart_item.product.cost
            lineItem.save()
        
        order_form = OrderForm()
        payment_form = PaymentForm()
        return render(request, 'checkout/charge.template.html', {
            'order_form': order_form,
            'payment_form': payment_form,
            'amount': amount,
            'transaction': transaction,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })
    else:
        transaction_id = request.POST['transaction_id']
        transaction = Transaction.objects.get(pk=transaction_id)
        if transaction.status != 'pending':
            return HttpReponse("Transaction has expired already")
            
        #payment being processed
        stripeToken = request.POST['stripe_id']
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount = int(request.POST['amount']),
                    currency = 'sgd',
                    description = 'Payment',
                    card = stripeToken
                    )
                if customer.paid:
                    order = order_form.save(commit=False)
                    order.date = timezone.now()
                    order.save()
                    
                    transaction = Transaction.objects.get(pk=transaction_id)
                    transaction.status='approved'
                    transaction.save()
                    
                    #remove cart_items
                    cart_items = CartItem.objects.filter(owner=request.user).delete()
                    
                    return render(request, "checkout/payment_successful.template.html")
                else:
                    return messages.error(request, "Your card was declined")
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
        else:
            return render(request, 'checkout/charge.template.html', {
                'order_form': order_form,
                'payment_form': payment_form,
                'amount': amount,
                'publishable': settings.STRIPE_PUBLISHABLE_KEY
            })
        return render(request, 'checkout/charge.template.html', {
            'order_form': order_form,
            'payment_form': payment_form,
            'amount': amount,
            'publishable': settings.STRIPE_PUBLISHABLE_KEY
        })