from rest_framework import serializers
from .models import Cart

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Password should not be readable

    class Meta:
        model = Cart
        fields = ['id','userid','name', 'category', 'price', 'usedtime', 'description']
