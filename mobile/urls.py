from django.urls import path, include
from . import views


app_name = 'mobile'
urlpatterns = [
    path('', views.index, name="index"),
    path('check_new_posts/', views.update_posts_notification, name ="check_new_posts")
]