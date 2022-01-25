from rest_framework.serializers import ModelSerializer
from api.models import Log, Project


class LogSerializer(ModelSerializer):
    """ Serialize user object """
    class Meta:
        model = Log
        fields = ('event', 'created', 'project')


class ProjectSerializer(ModelSerializer):
    """ Serialize project object """
    class Meta:
        model = Project
        fields = ('id', 'name', 'users')
