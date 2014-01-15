from django.core.management import BaseCommand
from airports.models import City, Airport, Country

__author__ = '4ikist'


class Command(BaseCommand):
    args = 'file name and path'

    def handle(self, *args, **options):
        with open(args[0]) as fn:
            lines = fn.readlines()
            for line in lines:
                params = line.strip().split(',')
                #this 4 airports can add with hands
                if len(params) != 11:
                    continue
                air_id = int(params[0])
                air_name = params[1].strip('"')
                city = params[2].strip('"')
                country = params[3].strip('"')
                iata = params[4].strip('"')
                icao = params[5].strip('"')
                longt = float(params[6])
                latit = float(params[7])
                amcl = int(params[8])
                utc = float(params[9])
                xz = params[10].strip('"')
                try:
                    self.stdout.write('params: [%s] [%s] [%s] [%s] [%s] [%s] [%s] [%s] [%s] [%s] [%s]' % (
                        air_id, air_name, city, country, iata, icao, longt, latit, amcl, utc, xz))
                except Exception as e:
                    pass
                country_obj, _ = Country.objects.get_or_create(name=country)
                if not _:
                    country_obj.save()

                city_obj, _ = City.objects.get_or_create(name=city, country=country_obj)
                if not _:
                    city_obj.save()

                airport, _ = Airport.objects.get_or_create(id=air_id, name=air_name, iata=iata, icao=icao, utc=utc,
                                                           amcl=amcl, latitude=latit,
                                                           longitude=longt, xz=xz, city=city_obj)
                if not _:
                    airport.save()


