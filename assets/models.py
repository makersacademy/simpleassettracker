from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Asset(models.Model):
  AssetTag = models.CharField(max_length=30)
  DeviceType = models.CharField(max_length=30, default='Laptop')
  CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)
