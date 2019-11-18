from django.shortcuts import render
from .models import Menu


# Create your views here.
def menu(request):
    all_products = Menu.objects.all();
    return render(request, 'menu/menu_items.template.html', {
        'all_products': all_products
    })
