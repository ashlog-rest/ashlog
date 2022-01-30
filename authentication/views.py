from authentication.models import User
from authentication.permissions import IsUserOrReadyOnly
from authentication.serializers import TokenSerializer, UserSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenObtainView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer


class UserViewSet(ModelViewSet):
    """ Handle creating, updating and removing users """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsUserOrReadyOnly,
    ]
