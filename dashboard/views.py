from django.shortcuts import render, redirect
from assets.models import Asset

def dashboardPageView(response):
  asset_count = countAssets()
  laptop_count = countLaptops()
  return render(response, "dashboard/dashboard.html", {
  "asset_count": asset_count,
  "laptop_count": laptop_count
  })

def countAssets():
  return Asset.objects.count()

def countLaptops():
  return Asset.objects.filter(DeviceType="laptop").count()
