from django.urls import path
from .views import get_carts, create_carts, cart_detail

urlpatterns =[
    path('carts/', get_carts, name = 'get carts'),
    path('carts/create/', create_carts, name = 'create carts'),
    path('carts/<int:pk>/', cart_detail, name='cart-detail'),
]