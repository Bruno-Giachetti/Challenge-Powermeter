from rest_framework import serializers
from .models import Medidor, Medicion


class MedidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medidor
        fields = ('llaveIdentificadora', 'nombre')

class MedicionSerializer(serializers.HyperlinkedModelSerializer):
    #medidores = serializers.SlugRelatedField(many=True, read_only=True,slug_field="nombre")
    medidor = MedidorSerializer(many = False)
    class Meta:
        model = Medicion
        fields = ('fechaYHora', 'consumo', 'medidor')