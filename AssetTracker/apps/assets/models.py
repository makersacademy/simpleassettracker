from django.db import models
from django.contrib.auth.models import User
from AssetTracker.apps.companies.models import Company

# Create your models here.

class Asset(models.Model):
  AssetTag = models.CharField(max_length=30)
  DeviceType = models.CharField(max_length=30, default='Laptop')
  DeviceModel = models.CharField(max_length=30, default="unassigned")
  AssetStatus = models.CharField(max_length=30, default='Ready')
  SerialNumber = models.CharField(max_length=64, unique=True)
  CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
  Company = models.ForeignKey(Company, on_delete=models.CASCADE)
  AssetCondition = models.CharField(max_length=30, default='Good')
  ScreenSize = models.CharField(max_length=30, default="unassigned")
  HardDrive = models.CharField(max_length=30, default="unassigned")
  Ram = models.CharField(max_length=30, default="unassigned")
  Year = models.CharField(max_length=30, default="unassigned")

  class Meta:
    unique_together = ['AssetTag', 'Company',]
