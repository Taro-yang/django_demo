from webchat.views.websocket import WsConsumer
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'^ws/(?P<group>\w+)$', WsConsumer.as_asgi())
]
