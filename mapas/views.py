from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render, get_object_or_404
from mapas.models import Estados, SociodemografiaRmc, RestaurantesCampinas, FarmaciasRmc
from mapas.serializers import EstadosSerializer, RMC_Serializer, Restaurantes_Serializer, \
    Farmacia_Serializer
from rest_framework import generics
import geocoder


def select_pois(request, camada, object):
    # model = camada
    queryset = camada.objects.all()

    variable_column = 'gid'
    search_type = 'intersects'
    filter1 = variable_column + '__' + search_type
    filtro = SociodemografiaRmc.objects.get(geom__intersects=(camada.objects.get(geom__)))
    search_string = '2622,2623,2616,2680,2678'  # gids da tabela sociodemografiaRMC

    pontos = camada.filter(**{filter1: search_string})
    # pontos da camada que caem dentro dos polígonos cujos gids foram recebidos no object
    return pontos

# SELECT f.*
#   FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd
#   WHERE sd.gid IN (2622,2623,2616,2680,2678)
#   		AND ST_Intersects(sd.geom, f.geom) = true;


class Teste_RMC(generics.ListCreateAPIView):
    queryset = SociodemografiaRmc.objects.all()
    serializer_class = RMC_Serializer

    def get_queryset(self):
        qs = super().get_queryset()
        local = self.request.query_params.get('local', None)
        filtro = self.request.GET.getlist('filtro')
        print(filtro)

        if local:
            g = geocoder.google(local, key='AIzaSyCYiHZL4JLYBrDqquu3EeaErg8LiZ_WFPo')
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            ponto = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)

        for value in filtro:
            nome_coluna = value
            print(value)
            filtro_range = 10
            filter_string = nome_coluna + '__range'
            filtro = SociodemografiaRmc.objects.values_list(nome_coluna, flat=True).get(geom__intersects=ponto)
            search_string = (filtro - filtro_range, filtro + filtro_range)

            # filtro = SociodemografiaRmc.objects.values_list('ipc_ab', flat=True).get(geom__intersects=ponto)
            # qs = SociodemografiaRmc.objects.filter(ipc_ab__gte=filtro2 - 10000).filter(ipc_ab__lte=filtro2 + 10000)
            # qs = qs.filter(f25a60anos__range=filtro1 - 10, filtro1 + 10)

            qs = SociodemografiaRmc.objects.filter(**{
                filter_string: search_string})  # pontos da camada que caem dentro dos polígonos cujos gids foram recebidos no object

        return qs


class Lista_Farmacias(generics.ListCreateAPIView):
    queryset = FarmaciasRmc.objects.all()
    serializer_class = Farmacia_Serializer

    def get_queryset(self):
        qs = super().get_queryset()
        gid = self.request.query_params.get('gid', None)

        # if gid:
            # variable_column = 'gid'
            # search_type = 'intersects'
            # filter1 = variable_column + '__' + search_type
        list_gid = [2622, 2623, 2616, 2680, 2678]
        # for i in range(len(list_gid)):
        #     filtro = SociodemografiaRmc.objects.values_list('geom', named=True)\
        #         .filter(gid__contains=list_gid[i])
        #     print(filtro)
        #     qs = FarmaciasRmc.objects.filter(geom__intersects=filtro)
        #     print(qs)

        filtro = SociodemografiaRmc.objects.filter(gid__in=list_gid)
        print(filtro)
        qs = FarmaciasRmc.objects.filter(geom__intersects=filtro)

                # FarmaciasRmc.filter(**{filter1: search_string})

            # SELECT f.gid, f.name
            #   FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd
            #   WHERE sd.gid IN (2622,2623,2616,2680,2678)
            #   		AND ST_Intersects(sd.geom, f.geom) = true;

        return qs
