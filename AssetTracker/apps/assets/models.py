from django.db import models
from django.contrib.auth.models import User
from AssetTracker.apps.companies.models import Company

# Create your models here.
class Asset(models.Model):
	asset_tag = models.CharField(max_length=30)
	device_type = models.CharField(max_length=30, default='Laptop')
	device_model = models.CharField(max_length=30, default="unassigned")
	asset_status = models.CharField(max_length=30, default='Ready')
	serial_number = models.CharField(max_length=64, unique=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	asset_condition = models.CharField(max_length=30, default='Good')
	screen_size = models.CharField(max_length=30, default="unassigned")
	hard_drive = models.CharField(max_length=30, default="unassigned")
	ram = models.CharField(max_length=30, default="unassigned")
	year = models.CharField(max_length=30, default="unassigned")

	class Meta:
		unique_together = ['asset_tag', 'company',]
