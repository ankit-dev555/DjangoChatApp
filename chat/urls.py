from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.UserFormView.as_view(), name='reg'),
url(r'^list/$', views.rlist.as_view(), name='list'),

url(r'^(?P<room>\w+)/$', views.chatting, name='room'),
url(r'^(?P<room1>\w+)/video/$', views.videochat, name='Videochat'),
url(r'^/logout$', views.logout1, name='lt'),

]