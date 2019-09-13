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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views
from webapp.views import UploadView
from webapp import views
from django.conf.urls import handler404, handler500

schema_view = get_swagger_view(title='SbaClean API')
api_urlpatterns = [
    path('', schema_view),
    path('accounts/', include(('Accounts.urls', 'Accounts'), namespace='api-accounts')),
    path('address/', include(('Address.urls', 'Address'), namespace='api-address')),
    path('posts/', include(('Post.urls', 'Post'), namespace='api-posts')),
    path('anomalys/', include(('Anomaly.urls', 'Anomaly'), namespace='api-anomaly')),
    path('events/', include(('Event.urls', 'Event'), namespace='api-event')),
    path('mobile/', include('mobile.urls')),
    path('notification/', include('notification.urls')),

]

urlpatterns = [
                  path('', views.index),
                  path('login/', views.login, name='login'),
                  path('accounts/login/', views.login, name='login'),
                  path('register/', views.register, name='register'),
                  path('feed/', views.feed, name='feed'),
                  path('event/', views.event, name='event'),
                  path('profile/', views.profile, name='profile'),
                  path('post_details/', views.feed, name='post_details'),
                  path('social-auth/', views.social_auth, name='social_auth'),
                  path('', include('social_django.urls', namespace='social')),
                  path("logout/", views.logout, name="logout"),
                  path('', include('dashboard.urls', namespace='dashboard')),
                  path('api/upload-image', UploadView.as_view()),


    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/v1/', include(api_urlpatterns)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^like/$',views.like_post,name="like_post"),
    url(r'^dislike/$',views.dislike_post,name="dislike_post"),
    url(r'^signaled/$',views.signaled,name="signaled"),
    url(r'^post_delete/$',views.post_delete,name="post_delete"),
    url(r'^Myposts/$',views.Myposts,name="Myposts"),
    url(r'^Myreactions/$',views.Myreactions,name="Myreactions"),
    url(r'^comment_delete/$',views.comment_delete,name="comment_delete"),
    url(r'^create_comment/$',views.create_comment,name="create_comment"),
    url(r'^Participate/$',views.Participate,name="Participate")
    
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler404 = views.error_404
handler500 = views.error_500
