from django.db import models

# Create your models here.

class users(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    contact = models.BigIntegerField(null=False)
    password = models.CharField(max_length=20, null=False)
    
    class Meta:
        db_table = 'users'

class admin(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    email =  models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=20, null=False)

    
    class Meta:
        db_table = 'admin'

class products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category =  models.CharField(max_length=100, null=False, blank=False)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'products'

