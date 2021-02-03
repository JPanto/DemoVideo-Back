from django.conf.urls import url
from Videos.views import ListVideo


urlpatterns = [
    url(r'^api/videos/$', ListVideo.as_view(), name='lista_video'),
]
