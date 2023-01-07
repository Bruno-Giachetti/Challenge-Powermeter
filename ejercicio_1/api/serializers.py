from rest_framework import serializers
from .models import Medidor, Medicion, Unidades

class MedidorSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombre = serializers.CharField()

    def validate(self, data):
        try:
            Medidor.objects.get(llaveIdentificadora = data.get('llaveIdentificadora'))
        except:
            pass
        else:
            raise serializers.ValidationError("Esa llave ya esta utilizada!")
        return data
        

    def create(self, validated_data):
        medidor = Medidor(
        llaveIdentificadora = validated_data.pop('llaveIdentificadora'),
        nombre = validated_data.pop('nombre'),
        )
        medidor.save()
        return medidor


class MedicionSerializer(serializers.Serializer):
    fechaYHora = serializers.DateTimeField()
    consumo = serializers.FloatField()
    unidad = serializers.CharField(required = False)
    medidor = serializers.CharField()

    def validate(self, data):
        if(data.get('consumo')<0):
            raise serializers.ValidationError("Consumo menor a 0!")
        if(data.get('unidad')!='kwh' and data.get('unidad')):
            raise serializers.ValidationError("La unidad debe ser kwh!")
        try:
            Medidor.objects.get(llaveIdentificadora= data.get('medidor'))
        except:
            raise serializers.ValidationError("No existe ese medidor!")
        
        return data

    def create(self, validated_data):
        medicion = Medicion(
        medidor = Medidor.objects.get(llaveIdentificadora = validated_data.pop('medidor')),  
        fechaYHora = validated_data.pop('fechaYHora'),
        consumo = validated_data.pop('consumo'),
        )
        medicion.save()
        return medicion
    

    



class MedicionTotalSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombreMedidor = serializers.CharField()
    unidad = serializers.CharField()
    consumoTotal = serializers.FloatField()

class MedicionPromedioSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombreMedidor = serializers.CharField()
    unidad = serializers.CharField()
    consumoPromedio = serializers.FloatField()