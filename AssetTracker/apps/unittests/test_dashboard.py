from django.test import TestCase, Client
from ..dashboard.views import *
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company
from ..assets.models import Asset

class dotdict(dict):
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

class DashboardTest(TestCase):

  def setUp(self):
    self.client = Client()
    user = User.objects.create(username='testuser', password='12345', email='testuser@test.com', is_active=True)
    user.set_password('12345')
    user.save()
    company = Company(name="Poland")
    company.save()
    CompanyUser.objects.create(user=user, company=company)
    laptop = Asset(asset_tag='123', device_type='Laptop', asset_status='Ready', serial_number='456', created_by=user, company=company)
    laptop.save()
    self.client.login(username='testuser', password='12345')

  def test_count_zero_laptops(self):
    assets = []
    self.assertEquals(count_laptops(assets), 0)

  def test_count_one_laptop(self):
    asset = {'device_type': 'Laptop'}
    asset = dotdict(asset)
    self.assertEquals(count_laptops([asset]), 1)

  def test_do_not_count_mobiles(self):
    asset = {'device_type': 'Mobile'}
    asset = dotdict(asset)
    self.assertEquals(count_laptops([asset]), 0)
  
  def test_count_zero_mobiles(self):
    assets = []
    self.assertEquals(count_mobiles(assets), 0)
  
  def test_count_one_mobile(self):
    asset = {'device_type': 'Mobile'}
    asset = dotdict(asset)
    self.assertEquals(count_mobiles([asset]), 1)
  
  def test_do_not_count_laptops(self):
    asset = {'device_type': 'Laptop'}
    asset = dotdict(asset)
    self.assertEquals(count_mobiles([asset]), 0)
  
  def test_count_zero_assets(self):
    assets = []
    self.assertEquals(count_assets(assets), 0)
    
  def test_count_one_asset(self):
    assets = {'device_type': 'Laptop'}
    assets = dotdict(assets)
    self.assertEquals(count_assets([assets]), 1)

  def test_get_assets(self):
    user = User.objects.get(username='testuser')
    self.assertEquals(len(get_assets(user)), 1)

  def test_do_not_get_assets_from_different_company(self):
    user = User.objects.get(username='testuser')
    user1 = User.objects.create(username='user2', password='12345', email='testuser@test.com', is_active=True)
    user1.save()
    company1 = Company(name='England')
    company1.save()
    CompanyUser.objects.create(user=user1, company=company1)
    self.assertEquals(len(get_assets(user1)), 0)

  def test_dashboard_page_view(self):
    response = self.client.get('/dashboard', follow='true')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'dashboard/dashboard.html')
