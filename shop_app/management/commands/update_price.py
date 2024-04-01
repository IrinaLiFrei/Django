from django.core.management.base import BaseCommand
from shop_app.models import Product


class Command(BaseCommand):
    help = 'Updates product price by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID of the product to update')
        parser.add_argument('price', type=int, help='Updated price of the product')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        new_price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.price = new_price
        product.save()
        self.stdout.write(self.style.SUCCESS(f'The price was updated to {new_price}'))
