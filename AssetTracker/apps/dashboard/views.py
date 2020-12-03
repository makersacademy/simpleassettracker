from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..assets.models import Asset
from ..companyusers.models import CompanyUser

@login_required(login_url='/login')
def dashboard_page_view(response):
	user = response.user
	asset_counts = get_asset_counts(user)
	return render(response, "dashboard/dashboard.html", {
	"asset_count": asset_counts[0],
	"laptop_count": asset_counts[1],
	"mobile_count": asset_counts[2],
	})

def get_assets(user):
	current_company_id = CompanyUser.objects.get(user = user).company.id
	company_users = CompanyUser.objects.filter(company = current_company_id)
	def get_user_id(i):
		return i.user.id
	company_user_ids = list(map(get_user_id, company_users))
	return Asset.objects.filter(created_by__in=company_user_ids)

def count_assets(assets):
	return len(assets)

def count_laptops(assets):
	count = 0
	for i in range(len(assets)):
		if assets[i].device_type.lower() == "laptop":
			count += 1
	return count

def count_mobiles(assets):
	count = 0
	for i in range(len(assets)):
		if assets[i].device_type.lower() == "mobile":
			count += 1
	return count

def get_asset_counts(logged_user):
	asset_list = get_assets(logged_user)
	counts = []
	counts.append(count_assets(asset_list))
	counts.append(count_laptops(asset_list))
	counts.append(count_mobiles(asset_list))
	return counts
