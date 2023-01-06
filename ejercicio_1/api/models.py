from django.db import models

class Medidor(models.Model):

    llaveIdentificadora = models.CharField(max_length=64, primary_key=True, null= False)
    nombre = models.CharField(
        null=False,
        blank=False,
        max_length=64
    )


    
    def __str__(self):
        return self.nombre

class Medicion(models.Model):
    fechaYHora = models.DateTimeField()
    consumo = models.FloatField()
    medidor = models.ForeignKey(to=Medidor,on_delete=models.CASCADE)


    def __str__(self):
        return "Creado"