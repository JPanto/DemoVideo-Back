from django.conf.urls import url
from views import EventList, EventDetail

urlpatterns = [
    url(r'^api/event/$', EventList.as_view(), name='event_list'),
    url(r'^api/event/(?P<pk>[0-9]+)$', EventDetail.as_view(), name='event_detail'),
]
