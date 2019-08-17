from rest_framework import serializers
from Anomaly.models import Anomaly, AnomalySignal


class AnomalySerializer(serializers.ModelSerializer):

    class Meta:
        model = Anomaly
        fields = ('id', 'consulted_at', "consulted_by", "post")


class AnomalySignalSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnomalySignal
        fields = '__all__'
