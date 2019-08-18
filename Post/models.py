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
    image = models.CharField(max_length=255,
                             default='https://www.eltis.org/sites/default/files/styles/web_quality/public/default_images/photo_default_2.png')
    latitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_reactions(self):
        likes_count = Reaction.objects.filter(post=self.id, is_like=True).count()
        dislikes_count = Reaction.objects.filter(post=self.id, is_like=False).count()
        return likes_count - dislikes_count

    def get_user(self):
        user = MyUser.objects.get(id = self.post_owner.id)
        payload = {
            "id" : user.pk,
            "username" : user.username,
            "email" : user.email,
            
        }
        return payload

    def owner(self):
        return self.post_owner


class Comment(models.Model):
    comment_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def owner(self):
        return self.comment_owner
    
    def get_user(self):
        user = MyUser.objects.get(id = self.comment_owner.id)
        payload = {
            "id" : user.pk,
            "username" : user.username
        }

        return payload


class Reaction(models.Model):
    reaction_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE)
    is_like = models.BooleanField(null=False)

    def owner(self):
        return self.reaction_owner


def get_picture_path(instance, filename):
    return os.path.join('Posts', str(instance.id), filename)


class Picture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=255,
                                  default='https://summer.pes.edu/wp-content/uploads/2019/02/default-2.jpg')
