from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Cart
from .serializer import CartSerializers

@api_view(['GET'])
def get_carts(request):
    userid= request.query_params.get('userid')
    if userid is not None:
        products = Cart.objects.filter(userid=userid)
    else:
        products = Cart.objects.all()
    serializedData = CartSerializers(products, many=True).data
    return Response(serializedData)

@api_view(['POST'])
def create_carts(request):
    data = request.data
    serializer = CartSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def cart_detail(request, pk):
    try:
        product =  Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response({"error":"product now found."}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({"message":"Product deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)