from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView

from Accounts.models import MyUser
from .serializers import MyUserSerializer

UserModel = get_user_model()


class CreateUserView(CreateAPIView):
    model = MyUser
    serializer_class = MyUserSerializer


class ListUserView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = MyUserSerializer

    def get_queryset(self):
        qs = MyUser.objects.all()
        query_username = self.request.GET.get("username")
        query_phone = self.request.GET.get("phone")
        query_email = self.request.GET.get("email")
        query_first_name = self.request.GET.get("first_name")
        query_last_name = self.request.GET.get("last_name")

        if query_username is not None:
            qs = qs.filter(Q(username__exact=query_username)).distinct()

        if query_phone is not None:
            qs = qs.filter(Q(phone_number__exact=query_phone)).distinct()

        if query_email is not None:
            qs = qs.filter(Q(email__exact=query_email)).distinct()

        if query_first_name is not None:
            qs = qs.filter(Q(first_name__contains=query_first_name)).distinct()

        if query_last_name is not None:
            qs = qs.filter(Q(last_name__contains=query_last_name)).distinct()

        return qs


class UserRUView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

