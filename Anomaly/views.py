from django.db.models import Q

from .models import Anomaly
from .serializers import AnomalySerializer
from rest_framework import mixins, generics


class AnomalyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = AnomalySerializer

    def get_queryset(self):
        qs = Anomaly.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
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
