from django.db import models
from companies.models import Company
from django.contrib.auth.hashers import make_password

class UnauthorizedUser(models.Model):
  Username = models.CharField(max_length=30)
  Password = models.CharField(max_length=30)
  Email = models.CharField(max_length=60)
  Company = models.ForeignKey(Company, on_delete=models.CASCADE)
