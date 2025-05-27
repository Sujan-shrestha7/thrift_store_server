from rest_framework import serializers
from .models import Seller 

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id','full_name', 'address', 'contact', 'email', 'password']