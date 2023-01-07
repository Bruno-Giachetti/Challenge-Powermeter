from django.db import models
from dataclasses import dataclass
from enum import Enum

class Unidades(Enum):
    KW = 1

class Medidor(models.Model):

    llaveIdentificadora = models.CharField(max_length=64, primary_key=True, null= False)
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return self.nombre

class Medicion(models.Model):
    fechaYHora = models.DateTimeField()
    consumo = models.FloatField()
    medidor = models.ForeignKey(to=Medidor, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.consumo)

class MedicionTotal:
    consumoTotal : models.FloatField()
    class Meta:
        abstract = True  # no table for this class
        managed = False  # no database management