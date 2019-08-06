from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from django.db import connection
from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework.views import APIView

from pontosMultidrogas.models import FarmasMulti
from pontosMultidrogas.serializers import FarmasMultiSerializer
from rest_framework import generics
from django.shortcuts import render, render_to_response
import json


def index(request):
    cidade = request.GET.get('cidade')
    template_name = 'index.html'
    farmacias = serialize('geojson', FarmasMulti.objects.filter(nm_municip=cidade.upper()), geometry_field='geom',
                          fields=('nm_municip',))
    context = {
        'farmacias': farmacias
    }
    print(context)
    return render(request, template_name, context)


def pontos(request):
    cidade = request.GET.get('cidade')
    farmacias = serialize('geojson', FarmasMulti.objects.filter(nm_municip=cidade.upper()), geometry_field='geom',
                          fields=('nm_municip',))
    return HttpResponse(farmacias, content_type='json')


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


class Lista_Multi(generics.ListAPIView):
    serializer_class = FarmasMultiSerializer

    def get_queryset(self):
        cidade = self.kwargs['cidade']
        print(cidade)
        return FarmasMulti.objects.all().filter(nm_municip=cidade.upper())


class MapaView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MapaView, self).get_context_data(**kwargs)

    def interesting_area(request, cidade):
        farmacias = FarmasMulti.objects.filter(nm_municip=cidade.upper())
        return render_to_response('index.html', {'farmacias': farmacias})
