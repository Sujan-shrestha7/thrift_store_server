from django.db import models
from users.models import Users

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    usedtime = models.CharField(max_length=50)
    description = models.TextField()
    userid = models.ForeignKey(Users, related_name='products', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'products'
