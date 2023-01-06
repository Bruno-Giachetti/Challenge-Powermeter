from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics

from .serializers import MedidorSerializer, MedicionSerializer
from .models import Medidor, Medicion



class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class minimoConsumoViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer
    lookup_field = 'pk'

    def get_queryset(self, llave=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        llave = self.kwargs.get('llave', None)
        queryset = Medidor.objects.filter(llaveIdentificadora = llave)
        return queryset
    
