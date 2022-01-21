from django.urls import path
from .views import poll, long_poll, websocket

urlpatterns = [
    path('poll/', poll.home),
    path("poll/send/", poll.msg),
    path("poll/get_msg/", poll.get_msg),
    path('long_poll/', long_poll.home),
    path("long_poll/send/", long_poll.msg),
    path("long_poll/get_msg/", long_poll.get_msg),
    path("websocket/", websocket.home),
]
