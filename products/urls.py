from django.urls import path
from .views import get_products, create_products, product_detail

urlpatterns =[
    path('products/', get_products, name = 'get products'),
    path('products/create/', create_products, name = 'create products'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
]