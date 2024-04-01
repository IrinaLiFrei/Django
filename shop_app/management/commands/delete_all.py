from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Deletes all data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS(f'Deleting objects...'))
        Client.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
        Order.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Objects deleted!'))
