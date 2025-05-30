from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import OrdersSerializer
from .models import Orders

@api_view(['GET'])
def get_order(request):
    sellerid= request.query_params.get('sellerid')
    if sellerid is not None:
        order = Orders.objects.filter(sellerid=sellerid)
    else:
        order = Orders.objects.all()
    serializer = OrdersSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_orders(request):
    data = request.data
    serializer = OrdersSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def order_detail(request, pk):
    try:
        order_instance = Orders.objects.get(pk=pk)
    except Orders.DoesNotExist:
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == 'PUT':
        serializer = OrdersSerializer(order_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # Changed to elif for clarity
        order_instance.delete()
        return Response({"message": "Order deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT) # Corrected "Category" to "Order"