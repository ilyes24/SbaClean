from django.urls import path, include
from Anomaly.Api.api import AnomalyAPIView, AnomalyRudView, AnomalySignalAPIView, AnomalySignalRudView


api_urlpatterns = [
    path('', AnomalyAPIView.as_view(), name='anomaly-listCreate'),
    path('<pk>', AnomalyRudView.as_view(), name='anomaly-rud'),
    path('signal', AnomalySignalAPIView.as_view(), name='signal-listCreate'),
    path('signal/<pk>', AnomalySignalRudView.as_view(), name='signal-rud')
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]