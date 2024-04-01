import random
from django.core.management.base import BaseCommand
from shop_app.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Fills the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='Number of objects to create')

    def handle(self, *args, **kwargs):
        number = kwargs.get('number')
        for i in range(1, number + 1):
            product = Product(name=f'Product_{i}', description=f'Product_bla-bla-bla_{i}',
                              price=random.randint(1000, 100_000), stock=random.randint(1, 100))
            product.save()

        for i in range(1, number + 1):
            client = Client(name=f'Name_{i}', email=f'Client_{i}@mail.com', phone=f'Phone_{i}',
                            address=f'Address_{i}')
            client.save()
            for _ in range(random.randint(1, 5)):
                order = Order.objects.create(client=client)
                order_products = random.choices(Product.objects.all(), k=random.randint(1, 5))
                for product in order_products:
                    order.products.add(product)
                order.total_price = sum(product.price for product in order.products.all())
                order.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created {number} clients, products, and orders'))
