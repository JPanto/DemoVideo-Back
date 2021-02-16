from django.conf.urls import url
from .views import ListFiles, DetailFiles

urlpatterns = [
    url(r'^api/files/$', ListFiles.as_view(), name='list_files'),
    url(r'^api/files/(?P<pk>[0-9]+)$', DetailFiles.as_view(), name='detail_file'),
]
