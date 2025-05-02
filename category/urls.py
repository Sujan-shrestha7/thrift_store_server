from django.urls import path
from .views import get_category, create_category, category_detail

urlpatterns =[
    path('category/',get_category, name = 'get cartegory'),
    path('category/create/', create_category, name='create category'),
    path('category/<int:pk>/', category_detail, name='cartegory-detail'),
]