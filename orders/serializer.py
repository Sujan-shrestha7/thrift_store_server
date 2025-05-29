from rest_framework import serializers
from .models import Orders
from users.models import Users
from products.models import Products
from sellers.models import Seller


class OrdersSerializer(serializers.ModelSerializer):
    userid = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    productid = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    sellerid = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    username = serializers.CharField(source='userid.fullname', read_only=True)
    useraddress = serializers.CharField(source='userid.address', read_only=True)
    usercontact = serializers.CharField(source='userid.contact', read_only=True)

    product_name = serializers.CharField(source='productid.name', read_only=True)
    product_price = serializers.CharField(source='productid.price', read_only=True)
    seller_name = serializers.CharField(source='sellerid.name', read_only=True)

    class Meta:
        model = Orders
        fields = [
            'id',
            'billno',
            'userid',
            'username',
            'useraddress',
            'usercontact',
            'productid',
            'product_name',
            'product_price',
            'sellerid',
            'seller_name',
        ]
        read_only_fields = ['billno']