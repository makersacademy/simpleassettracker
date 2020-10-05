from django.db import models
from django.contrib.auth.models import User
from AssetTracker.apps.companies.models import Company
from django.contrib.auth.hashers import make_password

class UnauthorizedUser(models.Model):
  User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
  