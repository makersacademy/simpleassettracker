from django import forms
from ..assets.models import Asset

class AssetForm(forms.ModelForm):
  class Meta:
    model = Asset
    fields = ("asset_tag", "device_type", "device_model", "asset_status", "serial_number", "asset_condition", "screen_size", "hard_drive", "ram", "year", "created_by", "company")
