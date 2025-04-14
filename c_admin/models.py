from django.db import models

# Create your models here.

class Admin(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    contact =  models.IntegerField(max_length=10,unique=True, null=False,
        error_messages={"unique": "A user with that contact already exists."}, blank=False)
    password = models.CharField(max_length=20, null=False)

    
    class Meta:
        db_table = 'admin'