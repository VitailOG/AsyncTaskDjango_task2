from django.urls import re_path

from .consumers import NotifyConsumer

websocket_urlpatterns = [
    re_path(r'^(?P<user_id>\d+)/$', NotifyConsumer.as_asgi()),
]
