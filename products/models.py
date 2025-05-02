from django.db import models
from users.models import Users

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    usedtime = models.CharField(max_length=50)
    description = models.TextField()
    userid = models.ForeignKey(Users, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return f"id:{self.id},name:{self.name}, category:{self.category}, price:{self.price}, usedtime:{self.usedtime}, description:{self.description}, userid:{self.userid}, image:{self.image}"