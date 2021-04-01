from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .serializers import *
from .models import *


# permission_class = permissions.IsAuthenticatedOrReadOnly
# Input in every class we need to protect
class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsManager(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ManagerViewSet(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerRetrieveView(generics.RetrieveAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerUpdateView(generics.UpdateAPIView):
    queryset = Manager.objects.all()
    serializer_class = CreateManagerSerializer
    permission_classes = (IsManager,)
    # permission_class = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Manager.objects.filter(user=user)

        raise PermissionDenied()


class ManagerCreateView(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = CreateManagerSerializer


# -----------------------------------

class ProducerViewSet(generics.ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerRetrieveView(generics.RetrieveAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class ProducerUpdateView(generics.UpdateAPIView):
    queryset = Producer.objects.all()
    serializer_class = CreateProducerSerializer


class ProducerCreateView(generics.CreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = CreateProducerSerializer


# ---------------------------------------

class ServiceViewSet(generics.ListAPIView):
    # queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()

        params = self.request.query_params

        price = params.get('price', None)
        producer = params.get('producer', None)
        manager = params.get('manager', None)

        if price:
            queryset = queryset.filter(price__lte=price)

        if producer:
            queryset = queryset.filter(producer__id=producer)

        if manager:
            queryset = queryset.filter(manager__id=producer)

        return queryset


class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer


# ---------------------------------------

class TagViewSet(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer


# ---------------------------------------

class OrderingViewSet(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingRetrieveView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingUpdateView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer


class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer


# ---------------------------------------

class MessageViewSet(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
