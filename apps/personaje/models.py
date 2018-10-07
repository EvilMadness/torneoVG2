from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.FileField(upload_to='personajes/')

    def __str__(self):
        return '{}'.format(self.nombre)
