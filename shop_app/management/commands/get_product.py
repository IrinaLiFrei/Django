from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Returns products with the price above a given value'

    def add_arguments(self, parser):
        parser.add_argument('value', type=int, help='Minimal price to return')

    def handle(self, *args, **kwargs):
        value = kwargs.get('value')
        products = Product.objects.filter(price__gte=value)
        for product in products:
            self.stdout.write(self.style.SUCCESS(f'{product}\n'))
