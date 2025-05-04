from rest_framework import serializers
from .models import Cart
from category.models import Category

class CartSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['id','userid','name', 'category', 'price', 'usedtime', 'description']
