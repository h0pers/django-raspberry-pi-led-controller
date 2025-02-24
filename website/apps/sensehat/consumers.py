import json

from channels.generic.websocket import WebsocketConsumer


class SensehatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        """
            Input data example:
            {
                1: (255, 0, 0),
                2: (255, 0, 0),
                3: (255, 0, 0),
            }
        """
        data = json.loads(text_data)
        self.send(json.dumps(data))
