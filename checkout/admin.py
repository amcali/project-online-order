from django.contrib import admin
from .models import Charge, Transaction, LineItem

# Register your models here.
# Models for charing customer for order, creating transaction for order, and creating line item for each item order
admin.site.register(Charge)
admin.site.register(Transaction)
admin.site.register(LineItem)