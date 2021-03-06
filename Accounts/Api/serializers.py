from rest_framework import serializers
from django.contrib.auth import get_user_model
from Address.models import City
from ..models import Notification
UserModel = get_user_model()


class MyUserSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(many=False, queryset=City.objects.all())

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            is_staff=validated_data['is_staff'],
            city=validated_data['city'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        user = UserModel.objects.get(username=instance)
        for attr, value in validated_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()
        return user

    def validate(self, value):
        if value['is_staff']:
            qs = UserModel.objects.filter(city__exact=value['city'], is_staff__exact=True, is_active__exact=True)
            qs = qs.exclude(username=value['username'])
            if qs.count() > 0:
                raise serializers.ValidationError("This city already has a responsible.")

        return value

    class Meta:
        model = UserModel
        fields = [
            "pk",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "city",
            "is_staff",
            "password",
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
