from django.urls import path
from authentication.views import TokenObtainView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
