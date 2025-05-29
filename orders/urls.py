from django.urls import path
from .views import get_order, create_orders, order_detail

urlpatterns =[
    path('orders/', get_order, name = 'get orders'),
    path('orders/create/', create_orders, name = 'create orders'),
    path('orders/<int:pk>/',order_detail, name='orders-detail'),
]