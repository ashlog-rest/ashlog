from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Log, Project
from api.serializers import LogSerializer, ProjectSerializer
from api.permissions import IsMemberOrReadOnly
from common.util import (
    send_discord,
    send_post_request,
    send_telegram,
)


class LogView(APIView):
    """ Handle creatining and listing logs """
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, project_id):
        if project_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        project = Project.objects.get(
            Q(users__in=[request.user]),
            id=project_id
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
            actions = request.data.get('actions')
            if actions:
                for a in actions:
                    action = a['action']
                    args = a['args']
                    if action == 'send_telegram':
                        send_telegram(
                            chat_id=args['chat_id'],
                            message=request.data.get('event'),
                            token=request.user.telegram_token,
                        )
                    elif action == 'send_discord':
                        send_discord(
                            channel_id=args['channel_id'],
                            message=request.data.get('event'),
                            token=request.user.discord_token,
                        )
                    elif action == 'send_post_request':
                        send_post_request(
                            url=args['url'],
                            data=args['data'],
                            headers=args['headers'],
                        )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):
    """ Handle creating, updating and deleting projects """
    permission_classes = [
        IsAuthenticated,
        IsMemberOrReadOnly,
    ]

    def get(self, request, project_id=None):
        projects = Project.objects.filter(
            Q(
                users__in=[request.user]
            )
        )
        if project_id is None:
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            project = projects.get(id=project_id)
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, project_id=None):
        project = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ProjectSerializer(
            data={
                'name': request.data.get('name'),
                'users': [request.user],
            },
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
