from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category =  models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=5,decimal_places=2, null=True)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'products'
