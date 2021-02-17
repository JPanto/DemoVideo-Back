from rest_framework.views import APIView
from rest_framework.response import Response

from .models import City, Country
from .serializers import CitySerializer, CountrySerializer


class ListCity(APIView):
    def get(self, request):
        cities = City.objects.all()
        city_json = CitySerializer(cities, many=True)
        return Response(city_json.data)


class ListCountry(APIView):
    def get(self, request):
        countries = Country.objects.all()
        country_json = CountrySerializer(countries, many=True)
        return Response(country_json.data)