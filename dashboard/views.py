from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assets.models import Asset

@login_required(login_url='/login')
def dashboardPageView(response):
  assetCounts = getAssetCounts()
  return render(response, "dashboard/dashboard.html", {
  "asset_count": assetCounts[0],
  "laptop_count": assetCounts[1],
  "mobile_count": assetCounts[2]
  })

def getAssets():
  return Asset.objects.all()

def countAssets(assets):
  return assets.count()

def countLaptops(assets):
  count = 0
  for i in range(len(assets)):
    if assets[i].DeviceType.lower() == "laptop":
      count += 1

  return count

def countMobiles(assets):
  count = 0
  for i in range(len(assets)):
    if assets[i].DeviceType.lower() == "mobile":
      count += 1

  return count

def getAssetCounts():
  assetList = getAssets()
  counts = []
  counts.append(countAssets(assetList))
  counts.append(countLaptops(assetList))
  counts.append(countMobiles(assetList))
  return counts
