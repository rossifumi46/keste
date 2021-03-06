from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'block/(?P<pk>[0-9]+)/$', views.BlockView.as_view(), name='index'),
    url(r'tutor/(?P<pk>[0-9]+)/$', views.TutorView.as_view(), name='index'),
    url(r'room/(?P<pk>[0-9]+)/$', views.RoomView.as_view(), name='index'),
    url(r'^search/$', views.search),
    url(r'free/$', views.free, name='free'),
    url(r'find/$', views.find, name='find'),
    url(r'^$', views.index),
]