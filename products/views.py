from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import Products
from .serializer import ProductSerializer

# Get All Users
@api_view(['GET'])
def get_products(request):
    users = Products.objects.all()
    serializedData = ProductSerializer(users, many=True).data
    return Response(serializedData)

# Create a New User
@api_view(['POST'])
def create_products(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
