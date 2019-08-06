from django.conf.urls import url

from . import views
from pontosMultidrogas.models import FarmasMulti
from pontosMultidrogas.views import Lista_Multi, index, pontos
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
  # url(r'^pontos/(?P<cidade>).+', Lista_Multi.as_view(), name='pontos'),
  url(r'^test/', views.index, name="index"),
  url(r'^pontos/', views.pontos, name="pontos"),
  url(r'^data/$',
      GeoJSONLayerView.as_view(model=FarmasMulti, properties=('nm_municip',)), name='data')
]