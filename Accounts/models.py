from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from Address.models import City


class MyUser(AbstractUser):
    phone_number = PhoneNumberField(blank=False, unique=True)
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def owner(self):
        return self


# is_staff = True                           is_staff = False
# User -> Mayor                             User -> Citizen
# phone_number -> City hall phone number    phone_number -> Citizen phone number
# city -> City hall city                    city -> Citizen city
# address -> City hall address              address -> Citizen address
# One User in the city. (validation in the serializer)
