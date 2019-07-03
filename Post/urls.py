from django.urls import path, include
from Post.Api.api import PostAPIView, PostRudView, CommentAPIView, CommentRudView, ReactionAPIView, ReactionRudView
from . import views

api_urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post-listCreate'),
    path('post/<pk>', PostRudView.as_view(), name='post-rud'),
    path('post/<pk>/comment', views.post_comments, name='post_comments'),


    path('comment/', CommentAPIView.as_view(), name='comment-listCreate'),
    path('comment/<pk>', CommentRudView.as_view(), name='comment-rud'),

    path('reaction/', ReactionAPIView.as_view(), name='reaction-listCreate'),
    path('reaction/<pk>', ReactionRudView.as_view(), name='reaction-rud'),
    path('reaction/user/<pk>', views.user_reactions, name='user_reactions'),

]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]