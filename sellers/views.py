from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password, check_password
from .models import Seller
from .serializer import SellerSerializer

# Get All Sellers
@api_view(['GET'])
def get_sellers(request):
    sellers = Seller.objects.all()
    serializedData = SellerSerializer(sellers, many=True).data
    return Response(serializedData)

# Seller Registration
class RegisterSellerView(APIView):
    def post(self, request):
        data = request.data
        data['password'] = make_password(data.get('password'))
        serializer = SellerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Seller Created Successfully!",
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Seller Login
class LoginSellerView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        seller = Seller.objects.filter(email=email).first()

        if seller and check_password(password, seller.password):
            refresh = RefreshToken.for_user(seller)
            serialized_seller = SellerSerializer(seller)
            return Response({
                "data": serialized_seller.data,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

# Seller Logout
class LogoutSellerView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
