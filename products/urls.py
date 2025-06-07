from django.urls import path
from .views import (
    get_products,
    create_products,
    product_detail,
    recommend_products,
    recommend_collaborative,
    interact_product,
)

urlpatterns = [
    path('products/', get_products, name='get_products'),
    path('products/create/', create_products, name='create_products'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/recommend/<int:product_id>/', recommend_products, name='content_recommendation'),
    # path('products/recommend-collaborative/', recommend_collaborative, name='collaborative_recommendation'),
    # path('products/interact/', interact_product, name='product_interact'),
]
