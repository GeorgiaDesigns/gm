from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from mapas.models import SociodemografiaRmc, RestaurantesCampinas, FarmaciasRmc
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


# class Lista_Farmacias(APIView):
#     def get(self, request):
#         gids = self.request.GET.getlist('gid')
#
#         if gids:
#             with connection.cursor() as cursor:
#                 for gid in gids:
#                     cursor.execute(
#                         "SELECT * FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd WHERE sd.gid IN"
#                         " (%s) AND ST_Intersects(sd.geom, f.geom) = true", [int(gid)])
#                     print(cursor)
#                     rows = cursor.fetchall()
#             result = []
#             keys = ('gid', 'name',)
#             for row in rows:
#                 result.append(dict(zip(keys, row)))
#                 print(result)
#         json_data = json.dumps(result)
#
#         return HttpResponse(json_data, content_type="application/json")


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
        query = "SELECT * FROM poi.farmacias_rmc f, dados_ibge.sociodemografia_rmc sd" 
                # " WHERE sd.gid IN (891, 1010, 1047, 1111, 1148, 1231, 1566, 1639, 1646, 1653, 1805, 1838, 1900, 1913, 1956, 1968, 2107, 2117, 2710, 2755, 2778, 2834, 3069, 3217, 3296, 3369, 3683, 3773, 3988, 4049, 4066, 4205, 306, 418, 464, 527, 641, 734, 805, 831, 858) AND ST_Intersects(sd.geom, f.geom) = true"

        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            result = []
            keys = ('gid', 'name',)
            for row in rows:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)

        return HttpResponse(json_data, content_type="application/json")

