
from django.urls import path, include
from .views import menu


urlpatterns = [
    path('', menu, name="menu"),
]
