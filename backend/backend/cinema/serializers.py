from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=68, min_length=6, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'username', 'password']
#
#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         username = attrs.get('username', '')
#
#         if not username.isalnum():
#             raise serializers.ValidationError('Username should only contain alphanumeric characters')
#         return attrs
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
#
#
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id', 'username', 'email', 'password']
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager
        fields = '__all__'


class CreateManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Producer
        fields = '__all__'


class CreateProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # producer = ProducerSerializer()
    # manager = ManagerSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class OrderingSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    # producer = ProducerSerializer()
    # manager = ManagerSerializer()

    class Meta:
        model = Ordering
        fields = '__all__'


class CreateOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    # producer = ProducerSerializer()
    # manager = ManagerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
