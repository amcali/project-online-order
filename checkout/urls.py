#checkout app urls
from django.urls import path, include
from .views import checkout, charge, cancel_charge

urlpatterns = [
    path("", checkout, name="checkout"),
    path("charge", charge, name="charge"),
    path("cancel_charge", cancel_charge, name="cancel_charge")
]

