from django.urls import path, include
from .views import checkout, charge, line_item

urlpatterns = [
    path("", checkout, name="checkout"),
    path("charge", charge, name="charge"),
    path("line_item", line_item, name="line_item")
]

