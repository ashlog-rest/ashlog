from authentication.serializers import TokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class TokenObtainView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer
