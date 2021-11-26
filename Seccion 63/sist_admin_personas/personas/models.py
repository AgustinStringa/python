from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.
"""
CLASE DE MODELO PARA INTERACTUAR CON LA DB
"""


class Domicilio(models.Model):
    calle = CharField(max_length=255, help_text='ej: san martin', null=1)
    nro_calle = IntegerField(help_text='ej: 1757', null=1)
    pais = CharField(max_length=255, help_text='ej: arg', null=1)

    def __str__(self) -> str:
        return f'{self.id} | {self.calle} {self.nro_calle} {self.pais}'


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = ForeignKey(Domicilio, on_delete=models.SET_NULL, null=1)

    # al redefinir el metodo __str__ cambia la froma de visualizarse las instancias
    # en el panel de admin de django
    def __str__(self):
        return f'{self.id} | {self.nombre} | {self.apellido} | {self.email} {self.domicilio}'
