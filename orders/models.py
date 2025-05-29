from django.db import models
from users.models import Users
from products.models import Products
from sellers.models import Seller

# Create your models here.

class Orders(models.Model):
    billno = models.IntegerField(unique=True, blank=False)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='orders', null=True)
    sellerid = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='orders', null=True)
    productid = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products', null=True)

    class Meta:
        db_table = 'orders'

    def save(self, *args, **kwargs):
        # Generate billno if it's not already set
        if not self.billno:
            last_order = Orders.objects.order_by('-billno').first()
            if last_order:
                self.billno = last_order.billno + 1
            else:
                # Starting billno if no orders exist
                self.billno = 1300200
        super().save(*args, **kwargs)

    def __str__(self):
        return f"billno: {self.billno}, sellerid: {self.sellerid}, userid: {self.userid}, productid:{self.productid}"