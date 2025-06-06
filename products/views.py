from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from django.contrib.auth.models import User

from .models import Products, ProductInteraction
from .serializer import ProductSerializer, ProductInteractionSerializer

# =========== Product Views ==================

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
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully!!"}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ========= Content-Based Recommendation View ====================
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

@api_view(['GET'])
def recommend_products(request, product_id):
    try:
        all_products = list(Products.objects.select_related('category').all())
        index = next((i for i, p in enumerate(all_products) if p.id == product_id), None)
        if index is None:
            return Response({'error': 'Product not found for recommendation.'}, status=status.HTTP_404_NOT_FOUND)

        documents = [
            f"{p.name} {p.description} {p.category.cat_name if p.category else ''}"
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

# =========== Collaborative Filtering (Implicit Feedback) ==========
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def interact_product(request, product_id):
    try:
        product = Products.objects.get(pk=product_id)
        ProductInteraction.objects.get_or_create(user=request.user, product=product)
        return Response({'message': 'Interaction recorded successfully!'}, status=status.HTTP_200_OK)
    except Products.DoesNotExist:
        return Response({'error': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommend_collaborative(request):
    try:
        interactions = ProductInteraction.objects.all()
        users = list(User.objects.all())
        products = list(Products.objects.all())

        user_index = {user.id: idx for idx, user in enumerate(users)}
        product_index = {product.id: idx for idx, product in enumerate(products)}

        matrix = np.zeros((len(users), len(products)))

        for interaction in interactions:
            u_idx = user_index[interaction.user.id]
            p_idx = product_index[interaction.product.id]
            matrix[u_idx][p_idx] = 1

        user_vector = matrix[user_index[request.user.id]]
        product_matrix = csr_matrix(matrix.T)
        scores = cosine_similarity(user_vector.reshape(1, -1), product_matrix.T).flatten()

        top_indices = scores.argsort()[::-1]

        recommended_ids = [products[i].id for i in top_indices if user_vector[i] == 0][:5]
        recommended_products = Products.objects.filter(id__in=recommended_ids)
        serialized = ProductSerializer(recommended_products, many=True).data
        return Response(serialized, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
