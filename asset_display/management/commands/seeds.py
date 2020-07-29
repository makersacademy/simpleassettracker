from django.core.management.base import BaseCommand, CommandError
from asset_display.models import Asset
from django.contrib.auth.models import User

import string, random

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "Seeds the database with usable data"

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")
        parser.add_argument('--number_of_users', type=int, help="Number of users")
        parser.add_argument('--assets_per_user', type=int, help="Assets per user")

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")
        run_seed(self, options['mode'], options['number_of_users'], options['assets_per_user'])
        self.stdout.write("Done.")

def clear_data():
    User.objects.all().delete()
    Asset.objects.all().delete()

def create_user():
    user = User(username=get_username(), password="password123")
    user.save()
    return user

def create_asset(user_instance):
    A = Asset(AssetTag=get_random_tag(), DeviceType=get_random_type(), CreatedBy=user_instance)
    A.save()

def create_objects(users, assets):
    for i in range(users):
        user = create_user()
        for j in range(assets):
            create_asset(user)

def get_random_tag():
    key=''
    for i in range(6):
        key += random.choice(string.ascii_letters + string.digits)
    return key

def get_random_type():
    assetTypes = ["Laptop", "Mobile", "Misc"]
    assetType = random.choice(assetTypes)
    return assetType

def get_username():
    usernames = ["admin", "james", "sarah", "richard", "ethan"]
    username = random.choice(usernames)
    usernames.remove(username)
    return username

def run_seed(self, mode, number_of_users, assets_per_user):
    clear_data()
    if mode == MODE_CLEAR:
        return
    create_objects(number_of_users, assets_per_user)


# Asset Types: ["Laptop", "Mobile", "Misc"]
# Usernames: ["admin", "james", "sarah", "richard", "ethan"]
#

