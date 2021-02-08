from django.conf.urls import url
from Videos.views import ListVideo, DetailVideo

urlpatterns = [
    url(r'^api/videos/$', ListVideo.as_view(), name='lista_video'),
    url(r'^api/videos/(?P<pk>[0-9]+)$', DetailVideo.as_view(), name='detail_video'),
]
