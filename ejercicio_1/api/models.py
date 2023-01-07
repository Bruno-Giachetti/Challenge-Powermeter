from django.db import models
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator
from dataclasses import dataclass
from enum import Enum

class Unidades(Enum):
    KWH = 1

class Medidor(models.Model):

    llaveIdentificadora = models.CharField(max_length=100, primary_key=True, null= False)
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.llaveIdentificadora

class Medicion(models.Model):
    fechaYHora = models.DateTimeField()
    consumo = models.FloatField(validators=[
            MinValueValidator(0.0),
        ],)
    unidad = models.CharField(default=Unidades.KWH.name.lower(), max_length=20)
    medidor = models.ForeignKey(to=Medidor, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(check = Q(unidad = 'kwh'), name = 'unidad_invalida_exc'),
        ]


    def __str__(self):
        return str(self.consumo)
