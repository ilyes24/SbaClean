from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from Address.models import City


class MyUser(AbstractUser):
    phone_number = models.BigIntegerField(blank=False, unique=True)
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    profile_pic_url = models.CharField(max_length=1000,
                                       default="https://avpn.asia/wp-content/uploads/2015/05/empty_profile.png")
    is_banned = models.BooleanField(default=False)

    def owner(self):
        return self

    def ban(self):
        self.is_banned = True
        self.save()


class Notification(models.Model):
    sender = models.ForeignKey(MyUser, related_name='user_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(MyUser, related_name='user_receiver', on_delete=models.CASCADE)
    message = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(null=True)


# is_staff = True                           is_staff = False
# User -> Mayor                             User -> Citizen
# phone_number -> City hall phone number    phone_number -> Citizen phone number
# city -> City hall city                    city -> Citizen city
# address -> City hall address              address -> Citizen address
# One User in the city. (validation in the serializer)
