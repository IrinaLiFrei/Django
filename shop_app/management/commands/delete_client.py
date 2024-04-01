from django.core.management.base import BaseCommand
from shop_app.models import Client


class Command(BaseCommand):
    help = 'Deletes client by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID of the client to delete')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
            self.stdout.write(self.style.SUCCESS(f'Client {pk} deleted'))
