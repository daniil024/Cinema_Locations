from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied

from .serializers import *
from .models import *


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'id': token.user_id, 'user': UserSerializer(user).data})


# permission_class = permissions.IsAuthenticatedOrReadOnly
# Input in every class we need to protect

# class RegisterView(generics.GenericAPIView):
#
#     serializer_class = RegisterSerializer
#
#     def post(self, request):
#         user = request.data
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         user_data = serializer.data
#
#         return Response(user_data, status=status.HTTP_201_CREATED)
#
#
# class UserViewSet(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


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
    # permission_classes = (IsManager,)
    # permission_class = permissions.IsAuthenticatedOrReadOnly

    # def get_queryset(self):
    #     user = self.request.user
    #
    #     if user.is_authenticated:
    #         return Manager.objects.filter(user=user)
    #
    #     raise PermissionDenied()


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
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Service.objects.all()

        params = self.request.query_params

        price_min = params.get('price_min', None)
        price_max = params.get('price_max', None)
        address = params.get('address', None)
        name = params.get('name', None)

        if price_min:
            queryset = queryset.filter(price__gte=price_min)

        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        if address:
            queryset = queryset.filter(address__icontains=address)

        if name:
            queryset = queryset.filter(Q(name__icontains=name) | Q(description__icontains=name))

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
