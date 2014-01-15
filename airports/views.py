from django.template.response import TemplateResponse
from airports.models import *
# Create your views here.


def get_country(request, c_id):
    country = Country.objects.get(id=c_id)
    cities = City.objects.filter(country=country).order_by('name')
    airports = Airport.objects.filter(city__in=cities).order_by('name')
    return TemplateResponse(request, 'country.html', {'country': country, 'cities': cities, 'airports': airports})


def get_city(request, c_id):
    city = City.objects.get(id=c_id)
    airports = Airport.objects.filter(city=city).order_by('name')
    return TemplateResponse(request, 'city.html', {'city': city, 'airports': airports})


def get_airport(request, air_id):
    result = Airport.objects.get(id=air_id)
    country = result.city.country
    return TemplateResponse(request, 'airport.html', {'airport': result, 'country': country})


def main(request):
    airports = Airport.objects.all().order_by('name')
    countries = Country.objects.all().order_by('name')
    cities = City.objects.all().order_by('name')
    return TemplateResponse(request, 'main.html', {'airports': airports, 'countries': countries, 'cities': cities})