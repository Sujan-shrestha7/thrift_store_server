from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Password should not be readable

    class Meta:
        model = Users
        fields = ['id', 'fullname', 'address', 'contact', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash password
        return super().create(validated_data)
