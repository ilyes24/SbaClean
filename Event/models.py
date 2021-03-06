from django.db import models
from Address.models import City
from Post.models import Post
from Accounts.models import MyUser


class Event(models.Model):
    post = models.ForeignKey(Post, related_name='event', on_delete=models.CASCADE)
    approved_by = models.ForeignKey(MyUser, related_name='approvedBy', on_delete=models.CASCADE, null=True)
    approved_at = models.DateTimeField(null=True)
    max_participants = models.IntegerField()
    starts_at = models.DateTimeField()
    status = models.CharField(max_length=255, default="pending")

    def owner(self):
        return self.post.owner

    def approve(self, approved_by, approved_at):
        self.approved_at = approved_at
        self.approved_by = approved_by
        self.status = 'approved'
        self.save()


class EventParticipation(models.Model):
    event = models.ForeignKey(Event, related_name='participatedEvent', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name='participatedUser', on_delete=models.CASCADE)
