from rest_framework import serializers
from .models import State, City


class StateSerializer(serializers.ModelSerializer):
    citys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = State
        fields = [
            'pk',
            'code',
            'name',
            'citys',
        ]


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = [
            'pk',
            'zip_code',
            'name',
            'state'
        ]
