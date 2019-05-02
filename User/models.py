from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class User(AbstractUser):
    is_mayor = models.BooleanField(default=False)
    is_citizen = models.BooleanField(default=False)


class Citizen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = PhoneNumberField(blank=False, unique=True)



