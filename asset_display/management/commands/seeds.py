from django.core.management.base import BaseCommand, CommandError
from asset_display.models import Asset
from django.contrib.auth.models import User

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "Seeds the database with usable data"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")
        run_seed(self, options['mode'])
        self.stdout.write("Done.")

def clear_data():
    User.objects.all().delete()
    Asset.objects.all().delete()

def create_user():
    B = User(username="three_admin", password="seed_admin123")
    B.save()
    return B

def create_asset(user):
    A = Asset(AssetTag="ABCDEFG", DeviceType="Laptop", CreatedBy=user)
    A.save()

def create_objects():
    create_asset(create_user())

def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_objects()

