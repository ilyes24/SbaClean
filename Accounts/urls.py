from django.urls import path, include
from .api import ListUserView, CreateUserView, UserRUView


api_urlpatterns = [
    path('', ListUserView.as_view(), name='user-list'),
    path('register/', CreateUserView.as_view(), name='user-create'),
    path('<pk>', UserRUView.as_view(), name='user-ru'),
]

urlpatterns = [
    path('', include(api_urlpatterns))
]
