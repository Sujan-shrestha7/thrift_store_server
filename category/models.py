from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        db_table = "category"
    def __str__(self):
        return f"cat_name:{self.cat_name}"