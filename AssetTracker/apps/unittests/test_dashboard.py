from django.test import SimpleTestCase
from ..dashboard.views import countLaptops, countMobiles

class dotdict(dict):
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __delattr__ = dict.__delitem__

class Dashboard(SimpleTestCase):

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
