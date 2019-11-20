from django.db import models
from datetime import datetime
from django.db.models.fields import DateField, TimeField

# Create your models here.
#This is for the cart
class CartItem(models.Model):
    product = models.ForeignKey('menu.Menu', on_delete=models.CASCADE)
    owner = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.product.name + " x " + str(self.quantity)