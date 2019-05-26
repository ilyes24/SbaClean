from django.urls import path, include
from Address.Api.api import StateAPIView, StateRudView, CityAPIView, CityRudView


api_urlpatterns = [
    path('state/', StateAPIView.as_view(), name='state-listCreate'),
    path('state/<pk>', StateRudView.as_view(), name='state-rud'),
    path('city/', CityAPIView.as_view(), name='city-listCreate'),
    path('city/<pk>', CityRudView.as_view(), name='city-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]
