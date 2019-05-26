from django.urls import path, include
from Event.Api.api import EventAPIView, EventRudView


api_urlpatterns = [
    path('', EventAPIView.as_view(), name='event-listCreate'),
    path('<pk>', EventRudView.as_view(), name='event-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]