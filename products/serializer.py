from rest_framework import serializers
from .models import Products
from category.models import Category
from users.models import Users

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.CharField(source='category.cat_name', read_only=True)

    userid = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    address = serializers.CharField(source='userid.address', read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
        # Optional explicit field list:
        # fields = ['id', 'name', 'category', 'category_name', 'price', 'usedtime', 'description', 'userid', 'user_address', 'image']
