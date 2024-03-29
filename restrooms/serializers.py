from .models import Toilet
from rest_framework import serializers

class ToiletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model=Toilet
        fields='__all__'