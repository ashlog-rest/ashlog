from django.urls import re_path
from web.consumers import LogConsumer

websocket_urlpatterns = [
    re_path(r'ws/project/(?P<project_id>\w+)/$', LogConsumer.as_asgi()),
]
