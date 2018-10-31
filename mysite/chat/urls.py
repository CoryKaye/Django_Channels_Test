#chat/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^join/(?P<room_name>[^/]+)/$', views.join, name='room'),
        url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
