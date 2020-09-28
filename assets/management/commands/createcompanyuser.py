from django.core.management.base import BaseCommand, CommandError
from assets.models import Asset
from companies.models import Company
from companyusers.models import CompanyUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import Argon2PasswordHasher

class Command(BaseCommand):
  help = "Creates a user to use the app with"

  def add_arguments(self, parser):
    parser.add_argument('--username', type=str, help="Username for user", default="admin")
    parser.add_argument('--password', type=str, help="Password for user", default="admin")
    parser.add_argument('--company_name', type=str, help="User's company", default="SAM")

  def handle(self, *args, **options):
    self.stdout.write("Creating user...")
    create_user(self, options['username'], options['password'], options['company_name'])
    self.stdout.write("Done.")
  
def create_user(self, username, password, company_name):
  user = User.objects.create(username=username)
  user.set_password(password)
  user.save()
  company = Company(Name=company_name)
  company.save()
  company_user = CompanyUser(User_id=user.id, Company_id=company.id)
  company_user.save()
  self.stdout.write(f'User {username} created with password {password}')
