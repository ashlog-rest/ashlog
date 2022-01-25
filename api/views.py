from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api.models import Log, Project
from api.serializers import LogSerializer, ProjectSerializer


class LogView(APIView):
    """ Handle creatining and listing logs """
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, project):
        if project is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        project = Project.objects.get(
            Q(users__in=[request.user]),
            id=project
        )
        if not project:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        logs = Log.objects.filter(project=project)
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LogSerializer(data=request.data)
        project = Project.objects.filter(
            Q(users__in=[request.user]),
            id=request.data.get('project')
        )
        if not project:
            return Response(status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(ModelViewSet):
    """ Handle creating, updating and deleting projects """
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Project.objects.filter(
            Q(
                users__in=[self.request.user]
            )
        )
