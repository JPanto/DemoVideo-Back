from django.conf.urls import url
from .views import EventAPI, EventList, EventDetail, EventUserAPI

urlpatterns = {
    url(r'^api/events/$', EventList.as_view(), name='event_list'),  # Get all event list
    url(r'^api/event_states/$', EventList.as_view(), name='event_states_list'),   # Get all event states list
    url(r'^api/event/(?P<pk>[0-9]+)$', EventDetail.as_view(), name='event_detail'),   # Get a specific event data
    url(r'^api/event/$', EventAPI.as_view(), name='event'),   # Post a event
    url(r'^api/event_user/$', EventUserAPI.as_view(), name='event_user'),   # Post a entry - Get all entry list
}
