from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.decorators import list_route

from mapas.models import Estados, SociodemografiaRmc
from mapas.serializers import EstadosSerializer, RMC_Serializer
from rest_framework import generics
import geocoder


def home(request):
    return render(request, 'index.html')


class ListaEstados(generics.ListCreateAPIView):
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        local = self.request.query_params.get('local', None)

        if local:
            g = geocoder.google(local, key='AIzaSyCYiHZL4JLYBrDqquu3EeaErg8LiZ_WFPo')
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            ponto = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)
            qs = Estados.objects.all().filter(geom__intersects=ponto)

        return qs


class Lista_RMC(generics.ListCreateAPIView):
    queryset = SociodemografiaRmc.objects.all()
    serializer_class = RMC_Serializer

    def get_queryset(self):
        qs = super().get_queryset()
        local = self.request.query_params.get('local', None)

        if local:
            g = geocoder.google(local, key='AIzaSyCYiHZL4JLYBrDqquu3EeaErg8LiZ_WFPo')
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            ponto = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)
            # qs = SociodemografiaRmc.objects.filter(geom__intersects=ponto)
            filtro1 = SociodemografiaRmc.objects.values_list('ipc_ab', flat=True).get(geom__intersects=ponto)
            filtro2 = SociodemografiaRmc.objects.values_list('f25a60anos', flat=True).get(geom__intersects=ponto)
            print(filtro1)

            qs = SociodemografiaRmc.objects.filter(ipc_ab__gte=filtro1 - 10000).filter(ipc_ab__lte=filtro1 + 10000)
            qs = qs.filter(f25a60anos__gte=filtro2 - 10).filter(f25a60anos__lte=filtro2 + 10)

        return qs


class Lista_Semelhantes(generics.ListCreateAPIView):
    queryset = SociodemografiaRmc.objects.all()
    serializer_class = RMC_Serializer

    def get_queryset(self):
        qs = super().get_queryset()

        pessoa2 = SociodemografiaRmc.objects.filter(ipc_ab__gte=74811.8-10000).filter(ipc_ab__lte=74811.8+10000)
        pessoa2 = pessoa2.filter(f25a60anos__gte=348-10).filter(f25a60anos__lte=348+10)
        pessoa2 = pessoa2.exclude(gid=2099)

        return pessoa2


