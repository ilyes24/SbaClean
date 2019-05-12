from django.db import models
from User.models import Citizen
from Address.models import State
import os


class Post(models.Model):
    post_owner = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment_owner = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    reaction_owner = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    is_like = models.BooleanField()


def get_picture_path(instance, filename):
    return os.path.join('Posts', str(instance.id), filename)


class Pictures(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo_path = models.ImageField(upload_to=get_picture_path, blank=True, null=True)
