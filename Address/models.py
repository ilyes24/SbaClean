from django.db import models


class State(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%d - %s' % (self.code, self.name)


class City(models.Model):
    zip_code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, related_name='citys', on_delete=models.CASCADE)
