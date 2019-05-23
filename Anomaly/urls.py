from django.urls import path, include
from django.conf.urls import url

apipatterns = [

]

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls'))
]