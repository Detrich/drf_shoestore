from django.core.management.base import BaseCommand, CommandError
from shoeapp.models import ShoeColor,ShoeType

class Command(BaseCommand):
    def handle(self, *args, **options):
        shoetypes = ['sneaker','boot','sandal','dress','other']
        shoecolor = ['Red','Orange','Green','Blue','Indigo','Violet','White','Black']
        for shoe in shoetypes:
            ShoeType.objects.create(style=shoe)
        for shoe in shoecolor:
            ShoeColor.objects.create(color_name=shoe)