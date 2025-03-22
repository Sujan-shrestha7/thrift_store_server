from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(
        max_length=15, 
        unique=True,
        help_text="Required. 15 characters or fewer.",
        error_messages={"unique": "A user with that contact already exists."},
    )
    password = models.CharField(max_length=255, null=True, blank=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"Name: {self.fullname}, Address: {self.address}, Contact: {self.contact}"


class Admin(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    email =  models.CharField(max_length=100,unique=True, null=False,
        error_messages={"unique": "A user with that contact already exists."}, blank=False)
    password = models.CharField(max_length=20, null=False)

    
    class Meta:
        db_table = 'admin'

class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category =  models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(decimal_places=2,max_digits=10, null=True)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'products'

class Orders(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders',null=True)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products',null=True)

    class Meta:
        db_table = 'orders'