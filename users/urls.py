from django.urls import path
from .views import get_users, RegisterView, LoginView,LogoutView

urlpatterns =[
    path('users/', get_users, name = 'get users')
]