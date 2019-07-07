from django.db.models import Q

from Anomaly.models import Anomaly
from .serializers import AnomalySerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import mixins, generics, permissions


class AnomalyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySerializer

    def get_queryset(self):
        user = self.request.user
        qs = Anomaly.objects.filter(
            post__city=user.city
        )
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(post__description__contains=query) |
                Q(consulted_at=query)
            ).distinct()
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


class AnomalyNonConsultedView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySerializer

    def get_queryset(self):
        user = self.request.user
        qs = Anomaly.objects.filter(
            post__city=user.city,
            consulted_at__isnull=True,
            consulted_by__isnull=True

        )
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(post__description__contains=query)
            ).distinct()
        return qs


class AnomalyConsultedView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySerializer

    def get_queryset(self):
        user = self.request.user
        qs = Anomaly.objects.filter(
            post__city=user.city,
            consulted_at__isnull=False,
            consulted_by__isnull=False

        )
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(post__description__contains=query)
            ).distinct()
        return qs

