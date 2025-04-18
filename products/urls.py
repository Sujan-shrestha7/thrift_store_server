from django.urls import path
from .views import get_products, create_products

urlpatterns =[
    path('products/', get_products, name = 'get products'),
    path('products/create/', create_products, name = 'create products')
]