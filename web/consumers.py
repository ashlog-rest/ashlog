import json
from channels.generic.websocket import AsyncWebsocketConsumer
from api.serializers import LogSerializer


class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = str(self.scope['url_route']['kwargs']['project_id'])
        await self.channel_layer.group_add(
            self.project_id,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.project_id,
            self.channel_name,
        )

    async def new_log(self, event):
        log = event['log']
        serializer = LogSerializer(log)
        await self.send(text_data=json.dumps({
            'log': serializer.data,
        }))
