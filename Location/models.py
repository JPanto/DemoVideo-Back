from django.db import models


class Country(models.Model):
    id_country = models.AutoField
    name = models.CharField(max_length=30)


class City(models.Model):
    id_city = models.AutoField
    name = models.CharField(max_length=50)
    id_country = models.ForeignKey('Country', on_delete=models.CASCADE)

