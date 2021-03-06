from django.db import models
from Address.models import City
from Post.models import Post
from Accounts.models import MyUser
from datetime import datetime, timedelta, timezone, tzinfo


class Anomaly(models.Model):
    post = models.ForeignKey(Post, related_name='anomaly', on_delete=models.CASCADE)
    consulted_by = models.ForeignKey(MyUser, related_name='consultedBy', on_delete=models.CASCADE, null=True)
    consulted_at = models.DateTimeField(null=True)
    signaled = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)

    def archive(self):
        self.archived = True
        self.consulted_at = datetime.now()
        self.save()

    def owner(self):
        return self.post.owner


class AnomalySignal(models.Model):
    anomaly = models.ForeignKey(Anomaly, related_name='signaledAnomaly', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name='signaledBy', on_delete=models.CASCADE)
    reported_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.anomaly.signaled = True
        super(AnomalySignal, self).save(*args, **kwargs)
