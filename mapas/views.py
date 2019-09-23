from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from mapas.models import SociodemografiaRmc, FarmaciasRmc, FarmaMulti, RmcHoteis, RestaurantesCampinas
from mapas.serializers import RMC_Serializer, Farmacia_Serializer, Multidrogas_Serializer, Hoteis_Serializer, \
    Restaurantes_Serializer
from rest_framework import generics
import geocoder
import json


def select_pois(request, camada):
    queryset = camada.objects.all()

    variable_column = 'gid'
    search_type = 'intersects'
    filter1 = variable_column + '__' + search_type
    # filtro = SociodemografiaRmc.objects.get(geom__intersects=(camada.objects.get(geom)))
    search_string = '2622,2623,2616,2680,2678'  # gids da tabela sociodemografiaRMC

    pontos = camada.filter(**{filter1: search_string})
    # pontos da camada que caem dentro dos polígonos cujos gids foram recebidos no object
    return render(request)


class Teste_RMC(generics.ListCreateAPIView):
    queryset = SociodemografiaRmc.objects.all()
    serializer_class = RMC_Serializer

    def get_queryset(self):
        qs = super().get_queryset()
        local = self.request.query_params.get('local', None)
        filtro = self.request.GET.getlist('filtro')
        slider = self.request.GET.getlist('range')

        if local:
            g = geocoder.google(local, key='AIzaSyCYiHZL4JLYBrDqquu3EeaErg8LiZ_WFPo')
            latitude = g.latlng[0]
            longitude = g.latlng[1]
            ponto = GEOSGeometry('POINT(' + str(longitude) + ' ' + str(latitude) + ')', srid=4326)

        for nome_coluna in filtro:
            for r in slider:
                filtro_range: int = int(r)
                filter_string = nome_coluna + '__range'
                filtro = SociodemografiaRmc.objects.values_list(nome_coluna, flat=True).get(geom__intersects=ponto)
                search_string = (filtro - filtro_range, filtro + filtro_range)

                qs = qs.filter(**{filter_string: search_string})

                print(qs)

        return qs


class Lista_POIs(APIView):
    def post(self, request):
        layer = self.request.query_params.get('layer', None)
        gids = self.request.GET.getlist('gid')

        if gids:
            stmt = (f"SELECT * FROM poi.{layer} f, dados_ibge.sociodemografia_rmc sd WHERE sd.gid IN"
                    " %s AND ST_Intersects(sd.geom, f.geom) = true")

            with connection.cursor() as cursor:
                cursor.execute(stmt, ([tuple(gids)]))
                rows = cursor.fetchall()

            result = []
            keys = ('gid', 'name',)
            for row in rows:
                result.append(dict(zip(keys, row)))
        json_data = json.dumps(result)

        return HttpResponse(json_data, content_type="application/json")
