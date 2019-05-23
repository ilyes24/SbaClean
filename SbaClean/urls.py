"""SbaClean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

api_urlpatterns = [
    path('accounts/', include(('Accounts.urls', 'Accounts'), namespace='api-accounts')),
    path('address/', include(('Address.urls', 'Address'), namespace='api-address')),
    path('anomalys/', include(('Anomaly.urls', 'Anomaly'), namespace='api-anomaly')),
    path('events/', include(('Event.urls', 'Event'), namespace='api-event')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(api_urlpatterns)),
]
