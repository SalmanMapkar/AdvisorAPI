from rest_framework import serializers
from .models import UserModel
from django.core.exceptions import ValidationError

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['Name', 'Email', 'Password']


class UserReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['UserId', "Password"]

class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['Email', 'Password']

