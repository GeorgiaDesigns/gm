from django.conf.urls import url
from django.urls import path

from mapas import views
from mapas.views import Lista_Farmacias, Teste_RMC, select_pois
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^RMC/', Teste_RMC.as_view()),
    url(r'^farmacias/', Lista_Farmacias.as_view()),
    path('pois/<camada>', views.select_pois, name='select_pois')
]
