from django.contrib import admin
from .models import Charge, Transaction

# Register your models here.
admin.site.register(Charge)
admin.site.register(Transaction)