from django.shortcuts import render, redirect
from assets.models import Asset

def dashboardPageView(response):
  asset_count = countAssets()
  return render(response, "dashboard/dashboard.html", {"asset_count": asset_count})

def countAssets():
  return Asset.objects.all().count()
