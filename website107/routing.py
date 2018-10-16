from chat import consumers
from django.conf.urls import include, url
from channels.routing import route
from django.contrib import admin


#application = ProtocolTypeRouter({})

channel_routing = [
route('websocket.connect', consumers.ws_connect_video,path=r'^/(?P<room1>[0-9]+)/video$'),
route('websocket.disconnect', consumers.ws_disconnect_video,path=r'^/(?P<room1>[0-9]+)/video$'),
route('websocket.receive', consumers.ws_receive_video,path=r'^/(?P<room1>[0-9]+)/video$'),
route('websocket.receive', consumers.ws_receive,path=r'^/(?P<room>[0-9]+)$'),
route('websocket.connect', consumers.ws_connect,path=r'^/(?P<room>[0-9]+)$'),
route('websocket.disconnect', consumers.ws_disconnect,path=r'^/(?P<room>[0-9]+)$')
]