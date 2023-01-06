from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from .serializers import MedidorSerializer, MedicionSerializer, MedicionTotalSerializer
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
    lookup_field = 'pk'

    def get_queryset(self, llave=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        llave = self.kwargs.get('llave', None)
        queryset = [Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').first()]
        print(type(queryset))
        return queryset

class maximoConsumoViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
    lookup_field = 'pk'

    def get_queryset(self, llave=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        llave = self.kwargs.get('llave', None)
        queryset = [Medicion.objects.filter(medidor__llaveIdentificadora = llave).order_by('consumo').reverse().first()]
        print(type(queryset))
        return queryset

class consumoTotalViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    lookup_field = 'pk'

    def get_queryset(self, llave=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        llave = self.kwargs.get('llave', None)
        queryset1 = Medicion.objects.filter(medidor__llaveIdentificadora = llave).aggregate(Sum('consumo'))
        queryset2 = Medidor.objects.filter(llaveIdentificadora = llave)
        queryset = queryset2.anno


        print(queryset1)
        print(queryset2)
        queryset = queryset2 | queryset1 
        queryset = Medidor.objects.filter(llaveIdentificadora = llave).update(queryset1)
        print(queryset)
        return HttpResponse.serialize(queryset1)
    
    
    
