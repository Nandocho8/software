from django.db import models
from django.conf import settings

# Create your models here.


class Comuna(models.Model):
    nombre = models.CharField('nombre comuna', max_length=200)

    def __str__(self):
        return self.nombre


class DatosUser(models.Model):
    correo = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    nombre = models.CharField('nombre', max_length=50)
    apellido_paterno = models.CharField('apellido_paterno', max_length=50)
    apellido_materno = models.CharField('apellido_materno', max_length=50)
    rut = models.CharField('rut', max_length=15)
    direccion = models.CharField('direccion', max_length=50)
    comuna = models.ForeignKey(Comuna,
                               on_delete=models.CASCADE,)

    def __str__(self):
        return self.nombre
