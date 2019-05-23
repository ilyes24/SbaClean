from rest_framework import serializers
from .models import Anomaly


class AnomalySerializer(serializers.ModelSerializer):

    class Meta:
        model = Anomaly
        fields = '__all__'
