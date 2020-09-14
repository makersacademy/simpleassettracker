from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Asset(models.Model):
  AssetTag = models.CharField(max_length=30)
  DeviceType = models.CharField(max_length=30, default='Laptop')
  AssetStatus = models.CharField(max_length=30, default='Ready')
  CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)