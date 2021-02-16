from rest_framework import serializers
from .models import City, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        country = Country
        fields = (
            'id_country',
            'name'
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        city = City
        fields = (
            'id_city',
            'name'
        )