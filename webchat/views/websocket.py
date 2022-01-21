from channels.generic.websocket import WebsocketConsumer
from django.shortcuts import render

USER = []


def home(request):
    uid = request.GET.get('uid')
    return render(request, 'websocket.html', {'uid': uid})


class WsConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        USER.append(self)
        self.accept()

    def websocket_receive(self, message):
        msg = message['text']
        for one in USER:
            one.send(msg)

    def websocket_disconnect(self, message):
        USER.remove(self)
