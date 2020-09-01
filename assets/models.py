from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

# Create your models here.

class Asset(models.Model):
  AssetTag = models.CharField(max_length=30)
  DeviceType = models.CharField(max_length=30, default='Laptop')
  CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
  Company = models.ForeignKey(Company, on_delete=models.CASCADE)