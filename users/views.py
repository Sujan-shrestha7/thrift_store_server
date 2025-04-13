from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import Users
from .serializer import UserSerializer

# Get All Users
@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    serializedData = UserSerializer(users, many=True).data
    return Response(serializedData)

# Create a New User
@api_view(['POST'])
def create_users(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Registration
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User Created Successfully!",
                "status": True,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
class LoginView(APIView):
    def post(self, request):
        data = request.data
        contact = data.get('contact') 
        password = data.get('password')
        user = Users.objects.filter(contact=contact).first()

        if user and check_password(password, user.password):  # Secure password check
            print("Password matched")

            # Create a fake Django User object for JWT
            class NewUser:
                id = user.id

            refresh = RefreshToken.for_user(NewUser()) 
            return Response({
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)

# User Logout
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
