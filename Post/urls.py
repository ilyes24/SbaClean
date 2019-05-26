from django.urls import path, include
from Post.Api.api import PostAPIView, PostRudView, CommentAPIView, CommentRudView, ReactionAPIView, ReactionRudView


api_urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post-listCreate'),
    path('post/<pk>', PostRudView.as_view(), name='post-rud'),

    path('comment/', CommentAPIView.as_view(), name='comment-listCreate'),
    path('comment/<pk>', CommentRudView.as_view(), name='comment-rud'),

    path('reaction/', ReactionAPIView.as_view(), name='reaction-listCreate'),
    path('reaction/<pk>', ReactionRudView.as_view(), name='reaction-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]