# models.py
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Role(models.Model):
    name = models.CharField(max_length=255)

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
