"""extendiendo el modelo de usuario"""
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=200, blank=True)