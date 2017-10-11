from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'block/^(?P<pk>[0-9]+)/$', views.Block.as_view(), name='index'),
    url(r'tutor/^(?P<pk>[0-9]+)/$', views.Tutor.as_view(), name='index'),
    url(r'room/^(?P<pk>[0-9]+)/$', views.Room.as_view(), name='index'),
    url(r'^search/$', views.search),
]