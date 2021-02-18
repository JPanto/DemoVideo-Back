from django.conf.urls import url
from .views import EventAPI, EventList, EventDetail

urlpatterns = [
    url(r'^api/events/$', EventList.as_view(), name='event_list'),
    url(r'^api/event/(?P<pk>[0-9]+)$', EventDetail.as_view(), name='event_detail'),
    url(r'^api/event/$', EventAPI.as_view(), name='event'),
]
