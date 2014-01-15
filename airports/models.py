from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2, blank=True, null=True)


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    iata = models.CharField(max_length=3, verbose_name="IATA", null=True, blank=True)
    icao = models.CharField(max_length=4, verbose_name='ICAO', null=True, blank=True)

    longitude = models.FloatField()
    latitude = models.FloatField()

    utc = models.FloatField()
    amcl = models.SmallIntegerField()

    xz = models.CharField(max_length=1)

    city = models.ForeignKey(City)




