from django.urls import path, include
from Accounts.Api.api import ListUserView, CreateUserView, UserRUView, UserRanking, NotificationAPIView, NotificationRudView


api_urlpatterns = [
    path('', ListUserView.as_view(), name='user-list'),
    path('register/', CreateUserView.as_view(), name='user-create'),
    path('<pk>', UserRUView.as_view(), name='user-ru'),
    path('ranking/', UserRanking.as_view(), name='user-ranking'),
    path('notification/', NotificationAPIView.as_view(), name='notif-list'),
    path('notification/<pk>', NotificationRudView.as_view(), name='notif-rud'),
]

urlpatterns = [
    path('', include(api_urlpatterns)),     # api url patterns
]
