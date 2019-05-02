from django.db import models


class State(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)


class City(models.Model):
    zip_code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    state = models.OneToOneField(State, on_delete=models.CASCADE, primary_key=True)
