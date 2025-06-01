from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Products
from django.db.models import Q
from .serializer import ProductSerializer

# ================== Existing Views ==================

@api_view(['GET'])
def get_products(request):
    sellerid = request.query_params.get('sellerid')
    product_name = request.query_params.get('product')
    
    products = Products.objects.all()

    if product_name:
        products = products.filter(
            Q(name__icontains=product_name) | Q(category__cat_name__icontains=product_name)
        )
    
    if sellerid is not None:
        products = products.filter(sellerid=sellerid)

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
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response({"error": "product not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {"message": "updated successfully !"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ================== Content-Based Recommendation View ==================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

@api_view(['GET'])
def recommend_products(request, product_id):
    try:
        all_products = list(Products.objects.select_related('category').all())
        index = next((i for i, p in enumerate(all_products) if p.id == product_id), None)
        if index is None:
            return Response({'error': 'Product not found for recommendation.'}, status=status.HTTP_404_NOT_FOUND)

        # Build corpus from key fields
        documents = [
            f"{p.name} {p.description} {p.usedtime} {p.category.cat_name if p.category else ''}"
            for p in all_products
        ]

        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(documents)
        cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

        similarity_scores = list(enumerate(cosine_similarities[index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]  # Top 5

        similar_products = [all_products[i[0]] for i in similarity_scores]
        serialized_data = ProductSerializer(similar_products, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
