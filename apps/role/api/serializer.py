# serializers.py
from rest_framework import serializers
from ..models import CustomUser, Role
from django.conf import settings

User = settings.AUTH_USER_MODEL

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = CustomUser
        fields = ['id', 'user', 'role']
