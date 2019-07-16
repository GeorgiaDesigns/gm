from rest_framework import serializers
from mapas.models import Estados, SociodemografiaRmc, RestaurantesCampinas, FarmaciasRmc


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
        #
        fields = '__all__'


class Farmacia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FarmaciasRmc
        # fields = ('gid', 'name')
        fields = '__all__'
