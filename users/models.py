from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)