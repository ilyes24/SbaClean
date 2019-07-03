from django.db import models
from Accounts.models import MyUser
from Address.models import State, City
import os


class Post(models.Model):
    title = models.TextField(max_length=255, default='Title')
    post_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    city = models.ForeignKey(City, related_name='location', on_delete=models.CASCADE)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def owner(self):
        return self.post_owner


class Comment(models.Model):
    comment_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def owner(self):
        return self.comment_owner


class Reaction(models.Model):
    reaction_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    is_like = models.BooleanField(null=False)

    def owner(self):
        return self.reaction_owner


def get_picture_path(instance, filename):
    return os.path.join('Posts', str(instance.id), filename)


class Pictures(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo_path = models.ImageField(upload_to=get_picture_path, blank=True, null=True)
