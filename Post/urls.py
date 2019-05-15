from django.conf.urls import url

from .views import PostAPIView, PostRudView, CommentAPIView, CommentRudView, ReactionAPIView, ReactionRudView

urlpatterns = [
    url(r'^post/$', PostAPIView.as_view(), name='post-listcreate'),
    url(r'^post/(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud'),
    url(r'^comment/$', CommentAPIView.as_view(), name='comment-listcreate'),
    url(r'^comment/(?P<pk>\d+)/$', CommentRudView.as_view(), name='comment-rud'),
    url(r'^reaction/$', ReactionAPIView.as_view(), name='reaction-listcreate'),
    url(r'^reaction/(?P<pk>\d+)/$', ReactionRudView.as_view(), name='reaction-rud')
]
