from django.conf.urls import url

from .views import EventAPIView, EventRudView

urlpatterns = [
    url(r'^event/$', EventAPIView.as_view(), name='event-listcreate'),
    url(r'^event/(?P<pk>\d+)/$', EventRudView.as_view(), name='event-rud'),
]
