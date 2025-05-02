from rest_framework import serializers
from .models import Products
from category.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    cat_name = serializers.CharField(source='category.cat_name', read_only=True)
    class Meta:
        model = Products
        fields = '__all__'
        # fields = ['id','name', 'price', 'cat_name','usedtime', 'description', 'userid','image']

