from django.shortcuts import render
from django.db.models import Sum, Avg
from django.forms.models import model_to_dict
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response

from .serializers import MedidorSerializer, MedicionSerializer,  MedicionTotalSerializer, MedicionPromedioSerializer
from .models import Medidor, Medicion, Unidades



class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer


    @action(detail=True, methods=['get'])
    def maximoConsumo(self, request, pk = None):
        llave = self.kwargs.get('pk', None)
        try:
            Medidor.objects.get(llaveIdentificadora= llave)
        except:
            raise serializers.ValidationError("No existe ese medidor!")
        if(not Medicion.objects.filter(medidor__llaveIdentificadora = llave)):
            raise serializers.ValidationError("Ese medidor no tiene mediciones")
        lista = Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').reverse().first()
        serializer = MedicionSerializer(lista, many = False)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def minimoConsumo(self, request, pk = None):
        llave = self.kwargs.get('pk', None)
        try:
            Medidor.objects.get(llaveIdentificadora= llave)
        except:
            raise serializers.ValidationError("No existe ese medidor!")
        if(not Medicion.objects.filter(medidor__llaveIdentificadora = llave)):
            raise serializers.ValidationError("Ese medidor no tiene mediciones")
        lista = Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').first()
        serializer = MedicionSerializer(lista, many = False)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def consumoTotal(self, request,  pk = None):
        llave = self.kwargs.get('pk', None)
        try:
            Medidor.objects.get(llaveIdentificadora= llave)
        except:
            raise serializers.ValidationError("No existe ese medidor!")
        
        medidor = Medidor.objects.get(llaveIdentificadora = llave)
        if(not Medicion.objects.filter(medidor__llaveIdentificadora = llave)):
            raise serializers.ValidationError("Ese medidor no tiene mediciones")
        resultado = Medicion.objects.filter(medidor__llaveIdentificadora = llave).aggregate(consumoTotal = Sum('consumo'))
        datos = {
                'consumoTotal' : resultado.get('consumoTotal'),
                'nombreMedidor' : medidor.nombre,
                'llaveIdentificadora' : medidor.llaveIdentificadora,
                'unidad' : Unidades.KWH.name.lower(),
        }
        serializer = MedicionTotalSerializer(datos, many = False)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def consumoPromedio(self, request,  pk = None):
        llave = self.kwargs.get('pk', None)
        try:
            Medidor.objects.get(llaveIdentificadora= llave)
        except:
            raise serializers.ValidationError("No existe ese medidor!")
        
        medidor = Medidor.objects.get(llaveIdentificadora = llave)
        if(not Medicion.objects.filter(medidor__llaveIdentificadora = llave)):
            raise serializers.ValidationError("Ese medidor no tiene mediciones")
        resultado = Medicion.objects.filter(medidor__llaveIdentificadora = llave).aggregate(consumoPromedio = Avg('consumo'))
        datos = {
                'consumoPromedio' : resultado.get('consumoPromedio'),
                'nombreMedidor' : medidor.nombre,
                'llaveIdentificadora' : medidor.llaveIdentificadora,
                'unidad' : Unidades.KWH.name.lower(),
        }
        serializer = MedicionPromedioSerializer(datos, many = False)
        return Response(serializer.data)




class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

