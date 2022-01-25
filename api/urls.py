from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import LogView, ProjectViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='projects')

urlpatterns = [
    path('log/', LogView.as_view()),
    path('project/<project>/log/', LogView.as_view()),
    path('', include(router.urls)),
]
