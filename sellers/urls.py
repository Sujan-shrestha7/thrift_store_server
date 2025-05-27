from django.urls import path
from .views import get_sellers, RegisterSellerView, LoginSellerView, LogoutSellerView

urlpatterns = [
    path('sellers/', get_sellers),
    path('sellers/register/', RegisterSellerView.as_view()),
    path('sellers/login/', LoginSellerView.as_view()),
    path('sellers/logout/', LogoutSellerView.as_view()),
]
