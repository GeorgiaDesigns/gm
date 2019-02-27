from rest_framework import serializers
from mapas.models import Empresas

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = ('nome', 'endereco')