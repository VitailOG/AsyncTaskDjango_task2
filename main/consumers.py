from channels.generic.websocket import AsyncJsonWebsocketConsumer

from django.contrib.auth import get_user_model


User = get_user_model()


class NotifyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f'user_{self.user_id}'
        print(self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def notify(self, event):
        message = event['message']
        await self.send_json({'message': message})
