from django.contrib.gis.geos import GEOSGeometry
from django.db import connection
from django.http import HttpResponse
from rest_framework.views import APIView

from pontosMultidrogas.models import FarmasMulti
from pontosMultidrogas.serializers import FarmasMultiSerializer
from rest_framework import generics
from django.shortcuts import render
import json


def index(request):
    return render(request, 'index.html')


# def dms2latlng(value):
#     geojson = dict(type='FeatureCollection', features=[])
#     props = dict(name=line.pop('StationName').title(),
#                  wmoid=wmoid,
#                  model='webmap.WeatherStation')
#
#     geom = dict(type='Point',
#                 coordinates=[lng, lat])
#     feature = dict(type='Feature',
#                    id=wmoid,
#                    geometry=geom,
#                    properties=props)
#     geojson['features'].append(feature)
#
#     json.dump(geojson, open(geojson_file, 'wb'))

def mapa(request):
    template_name = 'index.html'
    return render(request, template_name)


class Lista_Multi(generics.ListCreateAPIView):
    queryset = FarmasMulti.objects.all()
    serializer_class = FarmasMultiSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        cidade = self.request.query_params.get('cidade', None)

        if cidade:
            qs = FarmasMulti.objects.all().filter(nm_municip=cidade.upper())

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['cidade'] = 'Campinas'
        return ctx
