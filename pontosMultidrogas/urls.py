from django.conf.urls import url

from . import views
from pontosMultidrogas.models import FarmasMulti
from pontosMultidrogas.views import Lista_Multi
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
  url(r'^multi/', TemplateView.as_view(template_name='index.html'), name='index'),
  url(r'^pontos/', Lista_Multi.as_view(), name='pontos'),
  url(r'^data/$',
      GeoJSONLayerView.as_view(model=FarmasMulti), name='data')
]