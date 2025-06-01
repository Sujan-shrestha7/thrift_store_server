# products/recommendation.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .models import Products

def get_similar_products(product_id, top_n=5):
    products = list(Products.objects.select_related('category').all())
    
    index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    if index is None:
        return []

    # Combine fields to form a text corpus
    documents = [
        f"{p.name} {p.description} {p.usedtime} {p.category.name if p.category else ''}"
        for p in products
    ]

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    similarity_scores = list(enumerate(cosine_similarities[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    similar_products = [products[i[0]] for i in similarity_scores]
    return similar_products
