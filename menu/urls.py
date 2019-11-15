
from django.urls import path, include
from .views import menu_items


urlpatterns = [
    path('', menu_items, name="menu_items"),
    path('accounts/', include('accounts.urls')),
]
