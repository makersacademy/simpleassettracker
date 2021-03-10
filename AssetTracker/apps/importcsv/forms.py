from django import forms
from AssetTracker.apps.assets.models import Asset

class AssetForm(forms.ModelForm):
  
  serial_number = forms.CharField(required=False)
  screen_size = forms.CharField(required=False)
  hard_drive = forms.CharField(required=False)
  ram = forms.CharField(required=False)
  year = forms.CharField(required=False)
  imei = forms.CharField(required=False)
  storage = forms.CharField(required=False)
  colour = forms.CharField(required=False)

  class Meta:
    model = Asset
    fields = ("asset_tag", "device_type", "device_model", "asset_status", "serial_number", "asset_condition", "screen_size", "hard_drive", "ram", "year", "imei", "storage", "colour", "created_by", "company")
