from rest_framework import serializers
from pontosMultidrogas.models import FarmasMulti


class FarmasMultiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmasMulti
        fields = '__all__'
