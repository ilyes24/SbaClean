from rest_framework import serializers
from Post.models import Post, Comment, Reaction, Picture
from Anomaly.Api.serializers import AnomalySerializer

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reactions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reactions_count = serializers.SerializerMethodField()
    anomaly = AnomalySerializer(many = True, read_only = True)

    def get_reactions_count(self, obj):
        return obj.count_reactions()
    class Meta:
        model = Post
        fields =  (
            'id',
            'post_owner',
            'title',
            'comments',
            'reactions', 
            'anomaly',
            'description',
            'city',
            'longitude',
            'image',
            'latitude',
            'created_at',
            'reactions_count')
    



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'



class PictureSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Picture
        fields = '__all__'