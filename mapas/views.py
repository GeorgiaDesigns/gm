from django.shortcuts import render
from mapas.models import Empresas
from mapas.serializers import EmpresaSerializer
from rest_framework import generics

class ListaEmpresas(generics.ListCreateAPIView):
    queryset = Empresas.objects.all()
    serializer_class = EmpresaSerializer