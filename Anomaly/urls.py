from django.urls import path, include
from Anomaly.Api.api import AnomalyAPIView, AnomalyRudView


api_urlpatterns = [
    path('', AnomalyAPIView.as_view(), name='anomaly-listCreate'),
    path('<pk>', AnomalyRudView.as_view(), name='anomaly-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]