from django.conf.urls import url
from .views import ListCity, ListCountry

urlpatterns = [
    url(r'^api/city/$', ListCity.as_view(), name='list_city'),
    url(r'^api/country/$', ListCountry.as_view(), name='list_country'),
]