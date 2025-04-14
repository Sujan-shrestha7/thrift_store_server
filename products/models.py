from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category =  models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(decimal_places=2,max_digits=10, null=True)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'products'
