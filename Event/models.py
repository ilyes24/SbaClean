import datetime

from django.db import models
from Address.models import City
from Post.models import Post
from User.models import User


class Event(models.Model):
    post = models.ForeignKey(Post, related_name='event', on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, related_name='approvedBy', on_delete=models.CASCADE, null=True)
    approved_at = models.DateTimeField(null=True)
    max_participants = models.IntegerField()
    starts_at = models.DateTimeField()

    def approve(self, user):
        self.approved_by = user.id
        self.approved_at = datetime.datetime.now()
