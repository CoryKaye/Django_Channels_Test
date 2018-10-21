# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from .settings import *
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):

            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            msg_type = text_data_json['msg_type']


            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'msg_type': msg_type
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        msg_type = event['msg_type']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'msg_type': msg_type
        }))
