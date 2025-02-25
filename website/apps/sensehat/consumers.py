import json

from sense_hat import SenseHat
from channels.generic.websocket import WebsocketConsumer


class SensehatConsumer(WebsocketConsumer):
    sense = SenseHat()
    
    def connect(self):
        self.sense.clear()
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

        for index, rgb in data.items():
            self.sense.set_pixel(int(index) % 8, int(index) // 8, tuple(rgb))
            
        self.send(json.dumps(data))
