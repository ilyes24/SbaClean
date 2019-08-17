from django.urls import path, include
from Event.Api.api import EventAPIView, EventRudView, EventParticipationAPIView, EventParticipationRudView


api_urlpatterns = [
    path('', EventAPIView.as_view(), name='event-listCreate'),
    path('<pk>', EventRudView.as_view(), name='event-rud'),
    path('participate', EventParticipationAPIView.as_view(), name='eventParticipation-listCreate'),
    path('participate/<pk>', EventParticipationRudView.as_view(), name='eventParticipation-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]