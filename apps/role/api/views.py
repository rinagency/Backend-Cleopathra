# views.py
from rest_framework import generics
from django.contrib.auth.models import User
from ..models import CustomUser, Role
from .serializer import CustomUserSerializer, RoleSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
