from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..assets.models import Asset
from ..companyusers.models import CompanyUser

@login_required(login_url='/login')
def dashboardPageView(response):
  user = response.user
  assetCounts = getAssetCounts(user)
  return render(response, "dashboard/dashboard.html", {
  "asset_count": assetCounts[0],
  "laptop_count": assetCounts[1],
  "mobile_count": assetCounts[2],
  })


def getAssets(user):
  current_company_id = CompanyUser.objects.get(User = user).Company.id
  company_users = CompanyUser.objects.filter(Company = current_company_id)
  def get_user_id(i):
    return i.User.id
  company_user_ids = list(map(get_user_id, company_users))
  return Asset.objects.filter(CreatedBy__in=company_user_ids)

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

def getAssetCounts(logged_user):
  assetList = getAssets(logged_user)
  counts = []
  counts.append(countAssets(assetList))
  counts.append(countLaptops(assetList))
  counts.append(countMobiles(assetList))
  return counts
