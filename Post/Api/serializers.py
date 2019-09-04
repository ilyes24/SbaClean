from rest_framework import serializers
from Post.models import Post, Comment, Reaction, Picture
from Anomaly.Api.serializers import AnomalySerializer
from Event.Api.serializers import EventSerializer
from Accounts.Api.serializers import MyUserSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reactions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reactions_count = serializers.SerializerMethodField()
    anomaly = AnomalySerializer(many = True, read_only = True)
    event = EventSerializer(many = True, read_only = True)
    user = serializers.SerializerMethodField()

    def get_reactions_count(self, obj):
        return obj.count_reactions()
    
    def get_user(self, obj):
        return obj.get_user()
    
    class Meta:
        model = Post
        fields =  (
            'id',
            'post_owner',
            'user',
            'title',
            'comments',
            'reactions', 
            'anomaly',
            'event',
            'description',
            'city',
            'longitude',
            'image',
            'latitude',
            'created_at',
            'reactions_count')
    



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.get_user()
    
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'comment_owner',
            'post',
            'description',
            'created_at'
        )


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'



class PictureSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Picture
        fields = '__all__'