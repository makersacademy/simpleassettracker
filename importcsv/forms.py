from assets.models import Asset
from django import forms


class AssetForm(forms.ModelForm):
  class Meta:
    model = Asset
    fields = ("AssetTag", "DeviceType", "CreatedBy")
