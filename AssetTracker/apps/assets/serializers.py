from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('id', 'asset_tag', 'device_type', 'device_model', 'asset_status', 'created_by', 'serial_number', 'company', 'asset_condition', 'screen_size', 'hard_drive', 'ram', 'year')
