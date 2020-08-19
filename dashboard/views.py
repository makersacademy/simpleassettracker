from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assets.models import Asset

@login_required(login_url='/login')
def dashboardPageView(response):
  asset_count = countAssets()
  laptop_count = countLaptops()
  mobile_count = countMobiles()
  return render(response, "dashboard/dashboard.html", {
  "asset_count": asset_count,
  "laptop_count": laptop_count,
  "mobile_count": mobile_count
  })

def countAssets():
  return Asset.objects.count()

def countLaptops():
  return Asset.objects.filter(DeviceType="laptop").count()

def countMobiles():
  return Asset.objects.filter(DeviceType="mobile").count()
