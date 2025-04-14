from django.db import models
from users.models import Users
from products.models import Products

# Create your models here.

class Orders(models.Model):
    billno = models.IntegerField(max_length=7, unique=True,
        error_messages={"unique": "A user with that contact already exists."}, blank=False)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders',null=True)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products',null=True)

    class Meta:
        db_table = 'orders'