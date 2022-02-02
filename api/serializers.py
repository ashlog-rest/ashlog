from rest_framework.serializers import ModelSerializer
from api.models import Log, Project


class LogSerializer(ModelSerializer):
    """ Serialize log object """
    class Meta:
        model = Log
        fields = ('event', 'created', 'project')


class ProjectSerializer(ModelSerializer):
    """ Serialize project object """
    class Meta:
        model = Project
        fields = ('id', 'name', 'users')
        extra_kwargs = {
            'id': {'required': False},
            'name': {'required': False},
            'users': {'required': False},
        }
