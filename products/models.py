from django.db import models
from django.contrib.auth.models import User
from sellers.models import Seller
from category.models import Category

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    usedtime = models.CharField(max_length=50)
    description = models.TextField()
    sellerid = models.ForeignKey(Seller, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return f"id:{self.id}, name:{self.name}, category:{self.category}, price:{self.price}"

# ========== Collaborative Filtering Model (Implicit Feedback) ==========
class ProductInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    interacted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        db_table = 'product_interactions'

    def __str__(self):
        return f"{self.user.username} -> {self.product.name}"
