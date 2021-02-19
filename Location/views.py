from rest_framework.views import APIView
from rest_framework.response import Response

from .models import City, Country
from .serializers import CitySerializer, CountrySerializer


class ListCity(APIView):
    def get(self, request):
        cities = City.objects.all()
        city_json = CitySerializer(cities, many=True)
        return Response(city_json.data)


class CityAPI(APIView):
    def get(self, request, fk):
        """ Filter all cities by country """
        cities = City.objects.filter(id_country=fk)
        city_json = CitySerializer(cities, many=True)
        return Response(city_json.data, status=200)


class ListCountry(APIView):
    def get(self, request):
        countries = Country.objects.all()
        country_json = CountrySerializer(countries, many=True)
        return Response(country_json.data)
