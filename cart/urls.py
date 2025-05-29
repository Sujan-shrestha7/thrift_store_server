from django.urls import path
from .views import get_carts, create_carts, cart_detail


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('carts/', get_carts, name = 'get carts'),
    path('carts/create/', create_carts, name = 'create carts'),
    path('carts/<int:pk>/', cart_detail, name='cart-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)