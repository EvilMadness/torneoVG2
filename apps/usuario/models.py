from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    second_last_name = models.CharField(max_length=60)
    password = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
