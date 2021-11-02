from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'seed database'

    def handle(self, *args, **options):
        print('seeding database')
