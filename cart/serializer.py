from rest_framework import serializers
from .models import Cart
from category.models import Category

class CartSerializers(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    cat_name = serializers.CharField(source='category.cat_name', read_only=True)
    class Meta:
        model = Cart
        fields = ['id','userid','name', 'category', 'price','cat_name', 'usedtime', 'description']
