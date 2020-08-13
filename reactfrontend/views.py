from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/login')
def assets(request):
  return render(request, 'reactfrontend/assets.html')


def addAssets(request):
  return render(request, 'reactfrontend/addAssets.html')
