from rest_framework import serializers
from mapas.models import SociodemografiaRmc, RestaurantesCampinas,  RmcHoteis, FarmaMulti, FarmaciasRmc


class RMC_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SociodemografiaRmc
        fields = '__all__'


class Restaurantes_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantesCampinas
        fields = '__all__'


class Hoteis_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RmcHoteis
        fields = '__all__'


class Multidrogas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FarmaMulti
        fields = '__all__'


class Farmacia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FarmaciasRmc
        # fields = ('gid', 'name')
        fields = '__all__'
