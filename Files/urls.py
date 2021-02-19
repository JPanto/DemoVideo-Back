from django.conf.urls import url
from .views import ListFiles, DetailFiles, ListTypeFile

urlpatterns = [
    url(r'^api/files/$', ListFiles.as_view(), name='list_files'),   # Post a file - Get all file list
    url(r'^api/files/(?P<pk>[0-9]+)$', DetailFiles.as_view(), name='detail_file'),   # Get a specific file data
    url(r'^api/typefile/$', ListTypeFile.as_view(), name='list_type_file'),   # Get all event types list
]
