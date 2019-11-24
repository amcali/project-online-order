from django.db import models

# Create your models here.

""" Model for customer details for charging purposes"""
class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=6, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

""" Model for Line Items """
class LineItem(models.Model):
    product = models.ForeignKey('menu.Menu', on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, default=0)

    
    def __str__(self):
        return self.product.name + " : " + str(self.quantity)

""" Model for Transactions """
class Transaction(models.Model):
    status_options =[
        ('cancelled', "Cancelled"),
        ('pending', "Pending"),
        ('approved', "Approved"),
        ('rejected', "Rejected"),
        ('uncollected', "Uncollected"),
        ('collected', "Collected")
]

    charge = models.ForeignKey('Charge', on_delete=models.CASCADE, null=True)
    status = models.CharField(blank=False, choices=status_options, max_length=50)
    date = models.DateField()
    owner = models.ForeignKey("accounts.MyUser", on_delete=models.SET_NULL, null=True)
    line_items = models.ManyToManyField(LineItem)
    total_cost = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)

    def getTotalCostInDollars(self):
        return self.total_cost/100        
        

