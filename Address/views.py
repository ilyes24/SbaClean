from django.db.models import Q

from .models import City, State
from .serializers import CitySerializer, StateSerializer
from rest_framework import mixins, generics


class CityAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CitySerializer

    def get_queryset(self):
        qs = City.objects.all()
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


class CityRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StateAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = StateSerializer

    def get_queryset(self):
        qs = State.objects.all()
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


class StateRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = State.objects.all()
    serializer_class = StateSerializer
