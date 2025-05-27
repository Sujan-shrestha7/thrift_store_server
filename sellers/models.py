from django.db import models

class Seller(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    contact = models.CharField(max_length=10, blank=False, null=False)
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=False,
        null=False,
        error_messages={"unique": "A seller with this email address already exists."}
    )
    password = models.CharField(max_length=128, blank=False, null=False)

    class Meta:
        db_table = 'seller'

    def __str__(self):
        return f"id:{self.id}, full_name:{self.full_name}, address:{self.address}, contact:{self.contact}, email:{self.email}, password:{self.password}"
