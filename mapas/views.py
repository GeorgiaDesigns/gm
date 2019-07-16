from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.db.models import Subquery, OuterRef
from django.http import QueryDict, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from mapas.models import Estados, SociodemografiaRmc, RestaurantesCampinas, FarmaciasRmc
from mapas.serializers import EstadosSerializer, RMC_Serializer, Restaurantes_Serializer, Farmacia_Serializer
from rest_framework import generics
import geocoder
import json


def select_pois(request, camada, object):
    # model = camada
    queryset = camada.objects.all()

    variable_column = 'gid'
    search_type = 'intersects'
    filter1 = variable_column + '__' + search_type
    # filtro = SociodemografiaRmc.objects.get(geom__intersects=(camada.objects.get(geom)))
    search_string = '2622,2623,2616,2680,2678'  # gids da tabela sociodemografiaRMC

    pontos = camada.filter(**{filter1: search_string})
    # pontos da camada que caem dentro dos polígonos cujos gids foram recebidos no object
    return pontos


class Teste_RMC(generics.ListCreateAPIView):
    queryset = SociodemografiaRmc.objects.all()
    serializer_class = RMC_Serializer

    def get_queryset(self):
        qs = super().get_queryset()
        local = self.request.query_params.get('local', None)
        filtro = self.request.GET.getlist('filtro')

        if local:
            g = geocoder.google(local, key='AIzaSyCYiHZL4JLYBrDqquu3EeaErg8LiZ_WFPo')
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            ponto = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)

        for nome_coluna in filtro:
            filtro_range: int = 10
            filter_string = nome_coluna + '__range'
            filtro = SociodemografiaRmc.objects.values_list(nome_coluna, flat=True).get(geom__intersects=ponto)
            search_string = (filtro - filtro_range, filtro + filtro_range)

            qs = qs.filter(**{filter_string: search_string})
            print(qs)

        return qs


class JSONResponseMixin:

    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context


class Lista_Farmacias(JSONResponseMixin, APIView):
    serializer_class = Farmacia_Serializer

    def get(self, context, **response_kwargs):
        query = "SELECT * FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd" \
                " WHERE sd.gid IN (2622,2623,2616,2680,2678) AND ST_Intersects(sd.geom, f.geom) = true"

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            result = []
            keys = ('gid', 'name',)
            for row in rows:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

        return HttpResponse(json_data, content_type="application/json")


def get_queryset(self):
    qs = super().get_queryset()
    gid = self.request.GET.getlist('gid', None)

    # if gid:
    # variable_column = 'gid'
    # search_type = 'intersects'
    # filter1 = variable_column + '__' + search_type
    list_gid = [2622, 2623, 2616, 2680, 2678]
    # for gid in list_gid:
    #     filtro = SociodemografiaRmc.objects.values_list('geom', flat=True).filter(gid__contains=gid)
    #     qs = FarmaciasRmc.objects.filter(geom__within=filtro)
    #

    qs = SociodemografiaRmc.objects.values_list('geom', named=True).filter(gid__contains=list_gid).annotate(
        contained_points=Subquery(FarmaciasRmc.objects.filter(geom__within=OuterRef('geom')))
    )
    print(qs)
    # filtro = SociodemografiaRmc.objects.values_list('geom', flat=True).filter(gid__in=list_gid)
    # qs = FarmaciasRmc.objects.filter(geom__within=filtro)

    return qs

    # FarmaciasRmc.filter(**{filter1: search_string})

    # SELECT f.gid, f.name
    #   FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd
    #   WHERE sd.gid IN (2622,2623,2616,2680,2678)
    #   		AND ST_Intersects(sd.geom, f.geom) = true;
