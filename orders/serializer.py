from rest_framework import serializers
from .models import Orders
from users.models import Users
from cart.models import Cart
from sellers.models import Seller


class OrdersSerializer(serializers.ModelSerializer):
    userid = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    cartid = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    sellerid = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    username = serializers.CharField(source='userid.fullname', read_only=True)
    useraddress = serializers.CharField(source='userid.address', read_only=True)
    usercontact = serializers.CharField(source='userid.contact', read_only=True)

    product_name = serializers.CharField(source='cartid.name', read_only=True)
    product_price = serializers.CharField(source='cartid.price', read_only=True)
    product_image = serializers.CharField(source='cartid.image', read_only=True)
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
            'cartid',
            'product_name',
            'product_price',
            'sellerid',
            'seller_name',
            'product_image'
        ]
        read_only_fields = ['billno']