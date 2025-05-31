from django.db import models
from sellers.models import Seller
from category.models import Category

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    usedtime = models.CharField(max_length=50)
    description = models.TextField()
    sellerid = models.ForeignKey(Seller, related_name='users', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return f"id:{self.id},name:{self.name}, category:{self.category}, price:{self.price}, usedtime:{self.usedtime}, description:{self.description}, userid:{self.userid}, image:{self.image}"