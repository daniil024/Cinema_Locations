from rest_framework import serializers

from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password']


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
    producer = ProducerSerializer()
    manager = ManagerSerializer()

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
    producer = ProducerSerializer()
    manager = ManagerSerializer()

    class Meta:
        model = Ordering
        fields = '__all__'


class CreateOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordering
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    manager = ManagerSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

