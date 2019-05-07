from django.conf.urls import url

from .views import CityAPIView, StateAPIView,CityRudView, StateRudView

urlpatterns = [
    url(r'^city/$', CityAPIView.as_view(), name='city-listcreate'),
    url(r'^city/(?P<pk>\d+)/$', CityRudView.as_view(), name='city-rud'),
    url(r'^state/$', StateAPIView.as_view(), name='state-listcreate'),
    url(r'^state/(?P<pk>\d+)/$', StateRudView.as_view(), name='state-rud')
]
