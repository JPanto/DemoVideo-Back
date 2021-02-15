from django.conf.urls import url
from Files.views import ListFiles, DetailFiles

urlpatterns = [
    url(r'^api/files/$', ListFiles.as_view(), name='lista_files'),
    url(r'^api/files/(?P<pk>[0-9]+)$', DetailFiles.as_view(), name='detail_file'),
]
