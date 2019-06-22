from django.db.models import Q

from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from Accounts.models import MyUser
from django.contrib.auth import get_user_model

from .serializers import MyUserSerializer
from .permissions import IsOwnerOrReadOnly

UserModel = get_user_model()


class CreateUserView(CreateAPIView):

    model = MyUser
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyUserSerializer


class ListUserView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = MyUserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        qs = MyUser.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                Q(username__exact=query) |
                Q(phone_number__exact=query) |
                Q(email__exact=query) |
                Q(first_name__contains=query) |
                Q(last_name__contains=query)
            ).distinct()
        return qs


class UserRUView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [
        IsOwnerOrReadOnly
    ]