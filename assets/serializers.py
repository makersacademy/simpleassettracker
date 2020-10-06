from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ('id', 'AssetTag', 'DeviceType', 'DeviceModel', 'AssetStatus', 'CreatedBy',
		          'SerialNumber', 'Company', 'AssetCondition', 'ScreenSize', 'HardDrive', 'Ram', 'Year')
		