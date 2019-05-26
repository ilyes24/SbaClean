from rest_framework import serializers
from Address.models import State, City


class StateSerializer(serializers.ModelSerializer):
    citys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    # state = StateSerializer(read_only=True)

    class Meta:
        model = City
        fields = '__all__'
