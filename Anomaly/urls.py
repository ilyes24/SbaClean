from django.conf.urls import url

from .views import AnomalyAPIView, AnomalyRudView

urlpatterns = [
    url(r'^anomaly/$', AnomalyAPIView.as_view(), name='anomaly-listcreate'),
    url(r'^anomaly/(?P<pk>\d+)/$', AnomalyRudView.as_view(), name='anomaly-rud'),
]
