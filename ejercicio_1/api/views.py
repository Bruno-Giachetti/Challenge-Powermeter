from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import MedidorSerializer, MedicionSerializer
from .models import Medidor, Medicion

@api_view()
@permission_classes(AllowAny)

def previa(request):
    print(request.query_params)

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class minimoConsumoViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer
