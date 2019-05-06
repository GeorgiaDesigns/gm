from rest_framework import serializers
from mapas.models import Estados, SociodemografiaRmc, RestaurantesCampinas, EscolasParticualresSp


class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = '__all__'


class RMC_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SociodemografiaRmc
        fields = '__all__'


class Restaurantes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantesCampinas
        fields = '__all__'


class Escolas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EscolasParticualresSp
        fields = '__all__'
