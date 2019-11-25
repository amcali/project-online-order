from django.db import models

# Create your models here.
""" Model for menu items """
class Menu(models.Model):
    name = models.CharField(max_length=255, blank=False)
    sku = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    cost = models.IntegerField(blank=False)
    image = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.name + " : " + self.sku
        
    def getCostInDollars(self):
        return self.cost/100