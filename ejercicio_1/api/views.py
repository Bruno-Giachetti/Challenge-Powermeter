from django.shortcuts import render
from django.db.models import Sum, Avg
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from .serializers import MedidorSerializer, MedicionSerializer, MedicionTotalSerializer, MedicionPromedioSerializer
from .models import Medidor, Medicion



class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class minimoConsumoViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
    http_method_names = ['get']

    def get_queryset(self, llave=None):
        llave = self.kwargs.get('llave', None)
        queryset = [Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').first()]
        print(type(queryset))
        return queryset


class maximoConsumoViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
    http_method_names = ['get']

    def get_queryset(self, llave=None):
        llave = self.kwargs.get('llave', None)
        queryset = [Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').reverse().first()]
        print(type(queryset))
        return queryset

class consumoTotalViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedicionTotalSerializer
    http_method_names = ['get']

    def get_queryset(self, llave=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        llave = self.kwargs.get('llave', None)
        medidor = Medidor.objects.get(llaveIdentificadora = llave)

        resultados = Medicion.objects.filter(medidor__llaveIdentificadora = llave).aggregate(consumoTotal = Sum('consumo'))
        return [{
                'consumoTotal' : resultados.get('consumoTotal'),
                'nombreMedidor' : medidor.nombre,
                'llaveIdentificadora' : medidor.llaveIdentificadora,
        }]
    
class consumoPromedioViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedicionPromedioSerializer
    http_method_names = ['get']

    def get_queryset(self, llave=None):
        llave = self.kwargs.get('llave', None)
        medidor = Medidor.objects.get(llaveIdentificadora = llave)
        resultados = Medicion.objects.filter(medidor__llaveIdentificadora = llave).aggregate(consumoPromedio = Avg('consumo'))
        return [{
                'consumoPromedio' : resultados.get('consumoPromedio'),
                'nombreMedidor' : medidor.nombre,
                'llaveIdentificadora' : medidor.llaveIdentificadora,
        }]
    
    
