from django.db import models
from users.models import Users
from category.models import Category

class Cart(models.Model):
    # userid = models.ForeignKey(Users, related_name='carts', on_delete=models.CASCADE, null=True, blank=True)
    userid = models.ForeignKey(Users, related_name='carts', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(Category, related_name="cart_category", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'cart'
    
    def __str__(self):
        return f"userid:{self.userid},name:{self.name}, category:{self.category}, price:{self.price}, usedtime:{self.usedtime}"
