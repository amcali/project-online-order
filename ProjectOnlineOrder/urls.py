""" All app urls are included here """
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home/')),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menu.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
