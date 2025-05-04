from rest_framework import serializers
from .models import Category
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    cat_name = serializers.CharField(source='category.cat_name', read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

