from django.db.models import Q

from rest_framework import generics, mixins, permissions

from Address.models import City, State
from .serializers import CitySerializer, StateSerializer


class CityAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CitySerializer

    def get_queryset(self):
        qs = City.objects.all()
        query_name = self.request.GET.get("name")
        query_code = self.request.GET.get("zipcode")
        query_state = self.request.GET.get("state")
        if query_code is not None:
            qs = qs.filter(Q(zip_code__exact=query_code)).distinct()

        if query_name is not None:
            qs = qs.filter(Q(name__contains=query_name)).distinct()

        if query_state is not None:
            qs = qs.filter(Q(state__exact=query_state)).distinct()

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
        query_name = self.request.GET.get("name")
        query_code = self.request.GET.get("code")
        if query_code is not None:
            qs = qs.filter(Q(code__exact=query_code)).distinct()

        if query_name is not None:
            qs = qs.filter(Q(name__contains=query_name)).distinct()
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
