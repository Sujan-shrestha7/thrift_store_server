from django.db import models

# Create your models here.

class users(models.Model):
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


class admin(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    email =  models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=20, null=False)

    
    class Meta:
        db_table = 'admin'

class products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category =  models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(decimal_places=2,max_digits=10, null=True)
    usedtime = models.CharField(max_length=50, null=False)
    description =  models.CharField(max_length=255)

    class Meta:
        db_table = 'products'

