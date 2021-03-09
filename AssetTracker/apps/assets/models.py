from django.db import models
from django.contrib.auth.models import User
from AssetTracker.apps.companies.models import Company

# Create your models here.
class Asset(models.Model):
	asset_tag = models.CharField(max_length=30)
	device_type = models.CharField(max_length=30, default=None)
	device_model = models.CharField(max_length=30, default=None)
	asset_status = models.CharField(max_length=30, default='Ready')
	serial_number = models.CharField(max_length=64, unique=True, default=None, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	asset_condition = models.CharField(max_length=30, default='Good')
	screen_size = models.CharField(max_length=30, default=None, null=True)
	hard_drive = models.CharField(max_length=30, default=None, null=True)
	ram = models.CharField(max_length=30, default=None, null=True)
	year = models.CharField(max_length=30, default=None, null=True)
	imei = models.CharField(max_length=30, unique=True, default=None, null=True)
	storage = models.CharField(max_length=30, default=None, null=True)
	colour = models.CharField(max_length=30, default=None, null=True)

	class Meta:
		unique_together = ['asset_tag', 'company',]
