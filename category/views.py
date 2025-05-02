from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Category
from .serializer import CategorySerializer

@api_view(['GET'])
def get_category(request):
    category = Category.objects.all()
    serializedData = CategorySerializer(category, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_category(request):
    data = request.data
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({"error":"Category now found."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        category.delete()
        return Response({"message":"Category deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)