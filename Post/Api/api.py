from django.db.models import Q
from rest_framework import mixins, generics

from Post.models import Post, Comment, Reaction, Picture
from .serializers import PostSerializer, CommentSerializer, ReactionSerializer, PictureSerializer


class CommentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CommentSerializer

    def get_queryset(self):
        qs = Comment.objects.all()
        query_owner = self.request.GET.get("owner")
        query_post = self.request.GET.get("post")

        if query_owner is not None:
            qs = qs.filter(Q(comment_owner__exact=query_owner)).distinct()

        if query_post is not None:
            qs = qs.filter(Q(post__exact=query_post)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save(comment_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReactionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ReactionSerializer

    def get_queryset(self):
        qs = Reaction.objects.all()

        query_owner = self.request.GET.get("owner")
        query_post = self.request.GET.get("post")

        if query_owner is not None:
            qs = qs.filter(Q(reaction_owner__exact=query_owner)).distinct()

        if query_post is not None:
            qs = qs.filter(Q(post__exact=query_post)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save(reaction_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ReactionRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.all()

        query_owner = self.request.GET.get("owner")
        query_title = self.request.GET.get("title")
        query_city = self.request.GET.get("city")
        query_description = self.request.GET.get("description")
        query_anomaly = self.request.GET.get("anomaly")
        query_anomaly_owner = self.request.GET.get("anomalyOwner")

        if query_owner is not None:
            qs = qs.filter(Q(post_owner__exact=query_owner)).distinct()

        if query_title is not None:
            qs = qs.filter(Q(title__exact=query_title)).distinct()

        if query_city is not None:
            qs = qs.filter(Q(city__exact=query_city)).distinct()

        if query_description is not None:
            qs = qs.filter(Q(description__contains=query_description)).distinct()
        
        if query_anomaly is not None:
            qs = qs.filter(anomaly__gt = 0).filter(Q(title__contains = query_anomaly)).distinct()
        
        if query_anomaly_owner is not None:
            qs = qs.filter(anomaly__gt = 0).filter(Q(post_owner__exact=query_anomaly_owner)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save(post_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PictureAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PictureSerializer

    def get_queryset(self):
        qs = Picture.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(post_owner=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class PictureRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
