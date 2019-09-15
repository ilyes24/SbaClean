from django.urls import path, include
from . import views


app_name = 'notification'
urlpatterns = [
    path('', views.index, name="index"),
    #path('check_new_posts/', views.update_posts_notification, name ="check_new_posts"),
    path('send_notification/', views.send_new_anomaly_notification, name ="send_new_anomaly_notification"),
    path('new-user/', views.new_user, name ="new-user")


]