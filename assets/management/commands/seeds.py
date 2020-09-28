from django.core.management.base import BaseCommand, CommandError
from assets.models import Asset
from companies.models import Company
from companyusers.models import CompanyUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import Argon2PasswordHasher

import string, random

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'

class Command(BaseCommand):
  help = "Seeds the database with usable data"

  def add_arguments(self, parser):
    parser.add_argument('--mode', type=str, help="Mode")
    parser.add_argument('--number_of_users', type=int, help="Number of users", default=1)
    parser.add_argument('--assets_per_user', type=int, help="Assets per user", default=2)
    parser.add_argument('--company_name', type=str, help="Company to create users under", default='SAT')


  def handle(self, *args, **options):
    self.stdout.write("Seeding data...")
    run_seed(self, options['mode'], options['number_of_users'], options['assets_per_user'], options['company_name'])
    self.stdout.write("Done.")

def clear_data():
  User.objects.all().delete()
  Asset.objects.all().delete()
  Company.objects.all().delete()
  CompanyUser.objects.all().delete()

def create_user():
  username = get_username()
  password = "password1234"
  user = User.objects.create(username=username)
  user.set_password(password)
  user.save()
  return user

def create_asset(user_instance):
  A = Asset(AssetTag=get_random_tag(), DeviceType=get_random_type(), CreatedBy=user_instance)
  A.save()

def create_company(name):
  C = Company(Name=name)
  C.save()
  return C

def create_companyuser(user_instance, company_instance):
  CU = CompanyUser(User_id=user_instance.id, Company_id=company_instance.id)
  CU.save()

def create_objects(users, assets, company_name):
  company = create_company(company_name)
  for i in range(users):
    user = create_user()
    if i == 0:
      company.Owned_by=user
      company.save()
    create_companyuser(user, company)
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

usernames = ["admin", "james", "sarah", "richard", "ethan"]
def get_username():
  username = random.choice(usernames)
  usernames.remove(username)
  return username

def run_seed(self, mode, number_of_users, assets_per_user, company_name):
  clear_data()
  if mode == MODE_CLEAR:
    return
  create_objects(number_of_users, assets_per_user, company_name)


# Asset Types: ["Laptop", "Mobile", "Misc"]
# Usernames: ["admin", "james", "sarah", "richard", "ethan"]
