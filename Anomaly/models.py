import datetime

from django.db import models
from Address.models import City
from Post.models import Post
from User.models import User


class Anomaly(models.Model):
    post = models.ForeignKey(Post, related_name='anomaly', on_delete=models.CASCADE)
    consulted_by = models.ForeignKey(User, related_name='consultedBy', on_delete=models.CASCADE, null=True)
    consulted_at = models.DateTimeField(null=True)

    def consult(self, user):
        self.consulted_by = user.id
        self.consulted_at = datetime.datetime.now()
