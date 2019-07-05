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
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url
from webapp import views
api_urlpatterns = [
   
    path('accounts/', include(('Accounts.urls', 'Accounts'), namespace='api-accounts')),
    path('address/', include(('Address.urls', 'Address'), namespace='api-address')),
    path('posts/', include(('Post.urls', 'Post'), namespace='api-posts')),
    path('anomalys/', include(('Anomaly.urls', 'Anomaly'), namespace='api-anomaly')),
    path('events/', include(('Event.urls', 'Event'), namespace='api-event')),
    path('mobile/',include('mobile.urls'))

]

urlpatterns = [
    path('', views.index),
    path('login/', views.login, name='login'),
    path('register/', views.register,name='register'),
    path('feed/', views.feed,name='feed'),
    path('post_details/', views.feed,name='post_details'),
    path('social-auth/',views.social_auth, name='social_auth'),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/v1/', include(api_urlpatterns)),
    path('', include('social_django.urls', namespace='social')),
    path("logout/", views.logout, name="logout"),
]
