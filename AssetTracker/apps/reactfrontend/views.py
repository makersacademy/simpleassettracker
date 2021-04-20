from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')

def assets(request):
  return render(request, 'reactfrontend/assets.html')

def add_assets(request):
  return render(request, 'reactfrontend/addAssets.html')

def unauthorized_users(request):
  return render(request, 'reactfrontend/unauthorizedUsers.html')

def importcsv(request):
  return render(request, 'reactfrontend/importcsv.html')
  
def dashboard(request):
  return render(request, 'reactfrontend/dashboard.html')
