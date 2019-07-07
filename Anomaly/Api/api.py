from django.db.models import Q
from rest_framework import mixins, generics

from Anomaly.models import Anomaly, AnomalySignal
from .serializers import AnomalySerializer, AnomalySignalSerializer


class AnomalyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySerializer

    def get_queryset(self):
        qs = Anomaly.objects.all()

        query_post = self.request.GET.get("post")
        query_owner = self.request.GET.get("owner")
        query_title = self.request.GET.get("title")
        query_city = self.request.GET.get("city")
        query_description = self.request.GET.get("description")

        if query_post is not None:
            qs = qs.filter(Q(post__exact=query_post)).distinct()

        if query_owner is not None:
            qs = qs.filter(Q(post__post_owner__exact=query_owner)).distinct()

        if query_title is not None:
            qs = qs.filter(Q(post__title__exact=query_title)).distinct()

        if query_city is not None:
            qs = qs.filter(Q(post__city__exact=query_city)).distinct()

        if query_description is not None:
            qs = qs.filter(Q(post__description__contains=query_description)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class AnomalyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer


class AnomalySignalAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySignalSerializer

    def get_queryset(self):
        qs = AnomalySignal.objects.all()

        query_post = self.request.GET.get("post")
        query_owner = self.request.GET.get("owner")
        query_title = self.request.GET.get("title")
        query_city = self.request.GET.get("city")
        query_description = self.request.GET.get("description")
        query_signaled_by = self.request.GET.get("signaledBy")

        if query_post is not None:
            qs = qs.filter(Q(post__exact=query_post)).distinct()

        if query_owner is not None:
            qs = qs.filter(Q(post__post_owner__exact=query_owner)).distinct()

        if query_title is not None:
            qs = qs.filter(Q(post__title__exact=query_title)).distinct()

        if query_city is not None:
            qs = qs.filter(Q(post__city__exact=query_city)).distinct()

        if query_description is not None:
            qs = qs.filter(Q(post__description__contains=query_description)).distinct()

        if query_signaled_by is not None:
            qs = qs.filter(Q(user__exact=query_signaled_by)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class AnomalySignalRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = AnomalySignal.objects.all()
    serializer_class = AnomalySignalSerializer
