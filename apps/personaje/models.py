from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=10)