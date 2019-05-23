from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from Address.models import City


class MyUser(AbstractUser):
    phone_number = PhoneNumberField(blank=False, unique=True)
    city = models.ForeignKey(City, related_name='city', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
