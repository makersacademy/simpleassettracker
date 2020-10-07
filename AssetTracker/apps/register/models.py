from django.db import models
from django.contrib.auth.models import User
from ..companies.models import Company
from django.contrib.auth.hashers import make_password

class UnauthorizedUser(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
  