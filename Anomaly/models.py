from django.db import models
from Address.models import City
from Post.models import Post
from Accounts.models import MyUser


class Anomaly(models.Model):
    post = models.ForeignKey(Post, related_name='anomaly', on_delete=models.CASCADE)
    consulted_by = models.ForeignKey(MyUser, related_name='consultedBy', on_delete=models.CASCADE, null=True)
    consulted_at = models.DateTimeField(null=True)
    signaled = models.BooleanField(default = False)

    def owner(self):
        return self.post.owner


class AnomalySignal(models.Model):
    anomaly = models.ForeignKey(Anomaly, related_name='signaledAnomaly', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name='signaledBy', on_delete=models.CASCADE)
    reported_at = models.DateTimeField(null=True)
