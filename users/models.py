from django.db import models

class Users(models.Model):
    fullname = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(
        unique=True,
        help_text="Required. 15 characters or fewer.",
        error_messages={"unique": "A user with that contact already exists."},
    )
    password = models.CharField(max_length=255, null=True, blank=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"Name: {self.fullname}, Address: {self.address}, Contact: {self.contact}"
