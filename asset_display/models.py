from django.db import models
from django.contrib.auth.models import User

class Asset(models.Model):
  AssetTag = models.CharField(max_length=30)
  DeviceType = models.CharField(max_length=30)
  CreatedBy = models.ForeignKey(User, on_delete=models.CASCADE)