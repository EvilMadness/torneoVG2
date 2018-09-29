from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=60)