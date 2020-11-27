from django.test import TestCase, Client
from ..dashboard.views import *
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company

class dotdict(dict):
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

class Dashboard(TestCase):

  def setUp(self):
    self.client = Client()
    user = User.objects.create(username='user')
    user.set_password('12345')
    user.save()
    company = Company(name="Roland")
    company.save()
    CompanyUser.objects.create(user=user, company=company)
    self.client.login(username='user', password='12345')

  def test_count_laptops_zero(self):
    assets = []
    self.assertEquals(countLaptops(assets), 0)

  def test_count_laptops_one(self):
    asset = {'device_type': 'Laptop'}
    asset = dotdict(asset)
    self.assertEquals(countLaptops([asset]), 1)

  def test_do_not_count_mobiles(self):
    asset = {'device_type': 'Mobile'}
    asset = dotdict(asset)
    self.assertEquals(countLaptops([asset]), 0)
  
  def test_countMobiles_zero(self):
    assets = []
    self.assertEquals(countMobiles(assets), 0)
  
  def test_countMobiles_one(self):
    asset = {'device_type': 'Mobile'}
    asset = dotdict(asset)
    self.assertEquals(countMobiles([asset]), 1)
  
  def test_do_not_count_laptops(self):
    asset = {'device_type': 'Laptop'}
    asset = dotdict(asset)
    self.assertEquals(countMobiles([asset]), 0)
  
  def test_count_assets_zero(self):
    assets = []
    self.assertEquals(countAssets(assets), 0)
    
  def test_count_assets(self):
    assets = {'device_type': 'Laptop'}
    assets = dotdict(assets)
    self.assertEquals(countAssets([assets]), 1)

  def test_getAssets(self):
    user = User.objects.create(username='testuser', password='12345', email='testuser@test.com', is_active=False)
    user.save()
    company = Company(name="Poland")
    company.save()
    CompanyUser.objects.create(user=user, company=company)
    self.assertEquals(len(getAssets(user)), 0)

  # def test_getAssetCounts(self):
  #   user = {}
  #   dotdict(user)
  #   self.assertEquals(getAssetCounts([user]), 0)

  def test_dashboardPageView(self):
    response = self.client.get('/dashboard', follow='true')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'dashboard/dashboard.html')


