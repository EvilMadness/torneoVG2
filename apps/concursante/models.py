from django.db import models
from apps.escuela.models import Escuela
from apps.carrera.models import Carrera
from apps.personaje.models import Personaje

# Create your models here.
class Concursante(models.Model):
    nombre = models.CharField(max_length=30)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    id_escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    id_carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    id_personaje = models.ForeignKey(Personaje, on_delete=models.CASCADE)

