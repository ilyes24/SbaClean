from django.db import models
from Accounts.models import MyUser
# Create your models here.

class NotificationUser(models.Model):
    user = models.ForeignKey(MyUser, related_name="notificationUser", on_delete=models.CASCADE)
    user_opensignal_id = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)