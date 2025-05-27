from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Products
from .serializer import ProductSerializer

@api_view(['GET'])
def get_products(request):
    sellerid= request.query_params.get('sellerid')
    if sellerid is not None:
        products = Products.objects.filter(sellerid=sellerid)
    else:
        products = Products.objects.all()
    serializedData = ProductSerializer(products, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_products(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product =  Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response({"error":"product now found."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({"message":"Product deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{"message":"updated successfully !"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)