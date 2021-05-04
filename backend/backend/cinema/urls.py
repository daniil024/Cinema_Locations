from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    # path('register/', RegisterView.as_view(), name="register"),
    # path('users/all', UserViewSet.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/updateuser/', ChangePasswordView.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token/', obtain_auth_token, name='token'),
    path('auth/token/', CustomObtainAuthToken.as_view(), name='token'),
    path('auth/logout', Logout.as_view()),

    path('managers/<int:pk>', ManagerRetrieveView.as_view()),
    path('managers/update/<int:pk>', ManagerUpdateView.as_view()),
    path('managers/all', ManagerViewSet.as_view()),
    path('managers/new', ManagerCreateView.as_view()),

    path('producer/<int:pk>', ProducerRetrieveView.as_view()),
    path('producer/update/<int:pk>', ProducerUpdateView.as_view()),
    path('producer/all', ProducerViewSet.as_view()),
    path('producer/new', ProducerCreateView.as_view()),

    path('service/<int:pk>', ServiceRetrieveView.as_view()),
    path('service/update/<int:pk>', ServiceUpdateView.as_view()),
    path('service/all', ServiceViewSet.as_view()),
    path('service/new', ServiceCreateView.as_view()),

    path('tag/<int:pk>', TagRetrieveView.as_view()),
    path('tag/update/<int:pk>', TagUpdateView.as_view()),
    path('tag/all', TagViewSet.as_view()),
    path('tag/new', TagCreateView.as_view()),

    path('ordering/<int:pk>', OrderingRetrieveView.as_view()),
    path('ordering/update/<int:pk>', OrderingUpdateView.as_view()),
    path('ordering/all', OrderingViewSet.as_view()),
    path('ordering/new', OrderingCreateView.as_view()),

    path('message/<int:pk>', MessageRetrieveView.as_view()),
    path('message/update/<int:pk>', MessageUpdateView.as_view()),
    path('message/all', MessageViewSet.as_view()),
    path('message/new', MessageCreateView.as_view()),
]
