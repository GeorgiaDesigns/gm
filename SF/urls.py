"""SF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.urls import path

from mapas.views import ListaEstados, home, Lista_RMC, Lista_Semelhantes
from django.contrib import admin
from material.frontend import urls as frontend_urls


urlpatterns = [
    path('', home, name='home'),
    url(r'', include(frontend_urls)),

    url(r'^admin/', admin.site.urls),
    url(r'^estados/', ListaEstados.as_view()),
    url(r'^RMC/', Lista_RMC.as_view()),
    url(r'^semelhantes/', Lista_Semelhantes.as_view()),
]
