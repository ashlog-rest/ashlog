import json
import asyncio
from random import randint
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from api.models import Log
from api.serializers import LogSerializer


class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = str(self.scope['url_route']['kwargs']['project_id'])
        await self.channel_layer.group_add(
            self.project_id,
            self.channel_name,
        )
        await self.accept()

    async def new_log(self, event):
        log = event['log']
        serializer = LogSerializer(log)
        await self.send(text_data=json.dumps({
            'log': serializer.data,
        }))


"""         while True:
            await asyncio.sleep(5)

            obj = await database_sync_to_async(list)(Log.objects.filter(project=self.project_id))

            serializer = LogSerializer(obj, many=True)

            await self.send(
                text_data=json.dumps(serializer.data)
            ) """
