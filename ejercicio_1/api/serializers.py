from rest_framework import serializers
from .models import Medidor, Medicion, MedicionTotal


class MedidorSerializer(serializers.HyperlinkedModelSerializer):
    consumoTotal = serializers.HyperlinkedRelatedField(
        view_name='consumoTotalViewSet',
        lookup_field='consumo__sum',
        many=True,
        read_only=True,
        required = False,
    )
    class Meta:
        model = Medidor
        fields = ('llaveIdentificadora', 'nombre', 'consumoTotal')
        lookup_field = 'llaveIdentificadora'

class MedicionSerializer(serializers.HyperlinkedModelSerializer):
    #medidores = serializers.SlugRelatedField(many=True, read_only=True,slug_field="nombre")
    #medidor = MedidorSerializer(many = True)
    class Meta:
        model = Medicion
        fields = ('fechaYHora', 'consumo', 'medidor')

class MedicionTotalSerializer(serializers.Serializer):
    #medidores = serializers.SlugRelatedField(many=True, read_only=True,slug_field="nombre")
    #medidor = MedidorSerializer(many = True)
    consumo__sum = serializers.FloatField()