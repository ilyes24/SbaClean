from rest_framework import serializers
from Anomaly.models import Anomaly, AnomalySignal


class AnomalySerializer(serializers.ModelSerializer):

    class Meta:
        model = Anomaly
        fields = '__all__'


class AnomalySignalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnomalySignal
        fields = '__all__'
