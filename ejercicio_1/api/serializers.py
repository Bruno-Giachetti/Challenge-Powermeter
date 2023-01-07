from rest_framework import serializers
from .models import Medidor, Medicion, Unidades

'''
class MedidorSerializer(serializers.HyperlinkedModelSerializer):
    
    consumoTotal = serializers.HyperlinkedRelatedField(
        view_name='consumoTotalViewSet',
        lookup_field='consumo__sum',
        many=False,
        read_only=True,
        required = False,
    )
    
    class Meta:
        model = Medidor
        fields = ('llaveIdentificadora', 'nombre', 'consumoTotal')
'''
class MedidorSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombre = serializers.CharField()

    def create(self, validated_data):
        return Medidor.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.llaveIdentificadora = validated_data.get('llaveIdentificadora', instance.llaveIdentificadora)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()
        return instance


class MedicionSerializer(serializers.Serializer):
    fechaYHora = serializers.DateTimeField()
    consumo = serializers.FloatField()
    unidad = Unidades.KW
    medidor = serializers.CharField()

    def validate(self, data):
        if(data.get('consumo')<0):
            raise serializers.ValidationError("Consumo menor a 0!")
        return data

    def create(self, validated_data):
        medicion = Medicion(
        medidor = Medidor.objects.get(nombre = validated_data.pop('medidor')),  
        fechaYHora = validated_data.pop('fechaYHora'),
        consumo = validated_data.pop('consumo'),
        )
        medicion.save()
        return medicion
    



class MedicionTotalSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombreMedidor = serializers.CharField()
    unidad = Unidades.KW.name
    consumoTotal = serializers.FloatField()

class MedicionPromedioSerializer(serializers.Serializer):
    llaveIdentificadora = serializers.CharField()
    nombreMedidor = serializers.CharField()
    unidad = Unidades.KW.name
    consumoPromedio = serializers.FloatField()