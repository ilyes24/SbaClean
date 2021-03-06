from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.aggregates import Count
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from Post.models import Post
from Accounts.models import MyUser, Notification
from .serializers import MyUserSerializer, NotificationSerializer

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


class UserRanking(ListAPIView):
    lookup_field = 'pk'
    serializer_class = MyUserSerializer

    def get_queryset(self):
        qs = MyUser.objects.all()
        query_limit = int(self.request.GET.get('limit'))
        query_city = self.request.GET.get('city')
        query_user = self.request.GET.get('user')

        if query_limit is not None:
            if query_user is not None:
                # get the user
                user = MyUser.objects.filter(pk=query_user).first()

                # get all users of the same city
                users = qs.filter(city=user.city)

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                    Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)

                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]

                return users

            if query_city is not None:
                # get all users of the same city
                users = MyUser.objects.filter(city=query_city)

                # Then doing the calculations
                users = users.annotate(rank_point=(Count('post__reactions', filter=Q(post__reactions__is_like=True)) - (
                    Count('post__reactions', filter=Q(post__reactions__is_like=False))))).filter(rank_point__gt=0)

                # And finaly, order the results
                users = users.order_by('-rank_point')[:query_limit]

                return users


class NotificationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = NotificationSerializer

    def get_queryset(self):
        qs = Notification.objects.all()

        query_sender = self.request.GET.get("sender")
        query_receiver = self.request.GET.get("receiver")

        if query_sender is not None:
            qs = qs.filter(Q(sender__exact=query_sender)).distinct()

        if query_receiver is not None:
            qs = qs.filter(Q(receiver__exact=query_receiver)).distinct()

        return qs

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class NotificationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
