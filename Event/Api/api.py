from django.db.models import Q
from rest_framework import mixins, generics

from Event.models import Event, EventParticipation
from .serializers import EventSerializer, EventParticipationSerializer


class EventAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EventSerializer

    def get_queryset(self):
        qs = Event.objects.all()

        query_post = self.request.GET.get("post")
        query_date = self.request.GET.get("date")
        query_owner = self.request.GET.get("owner")
        query_title = self.request.GET.get("title")
        query_city = self.request.GET.get("city")
        query_description = self.request.GET.get("description")
        query_approved = self.request.GET.get("approved")
        query_starts_at = self.request.GET.get("start")

        if query_post is not None:
            qs = qs.filter(Q(post__exact=query_post)).distinct()

        if query_date is not None:
            qs = qs.filter(Q(starts_at__gt=query_date)).distinct()

        if query_owner is not None:
            qs = qs.filter(Q(post__post_owner__exact=query_owner)).distinct()

        if query_title is not None:
            qs = qs.filter(Q(post__title__exact=query_title)).distinct()

        if query_city is not None:
            qs = qs.filter(Q(post__city__exact=query_city)).distinct()

        if query_description is not None:
            qs = qs.filter(Q(post__description__contains=query_description)).distinct()

        if query_approved is not None:
            qs = qs.filter(Q(approved_by__isnull=False)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class EventRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventParticipationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EventParticipationSerializer

    def get_queryset(self):
        qs = EventParticipation.objects.all()

        query_event = self.request.GET.get("event")
        query_user = self.request.GET.get("user")

        if query_event is not None:
            qs = qs.filter(Q(event__exact=query_event)).distinct()

        if query_user is not None:
            qs = qs.filter(Q(user__exact=query_user)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class EventParticipationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = EventParticipation.objects.all()
    serializer_class = EventParticipationSerializer
