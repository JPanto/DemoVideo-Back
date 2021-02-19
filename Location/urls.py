from django.conf.urls import url
from .views import ListCity, ListCountry, CityAPI

urlpatterns = [
    url(r'^api/city/$', ListCity.as_view(), name='list_city'),  # Get all city list
    url(r'^api/country/$', ListCountry.as_view(), name='list_country'),  # Get all country list
    url(r'^api/cities/(?P<fk>[0-9]+)$', CityAPI.as_view(), name='cities_by_country'),  # Get all city list by
                                                                                       # specific country
]
