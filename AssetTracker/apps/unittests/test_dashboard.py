from django.test import SimpleTestCase
from ..dashboard.views import countLaptops

class Dashboard(SimpleTestCase):

  def test_countLaptops_zero(self):
    assets = []
    self.assertEquals(countLaptops(assets), 0)

  def test_countLaptops_one(self):
    class dotdict(dict):
      __getattr__ = dict.get
      __setattr__ = dict.__setitem__
      __delattr__ = dict.__delitem__

    asset = {'device_type': 'Laptop'}
    asset = dotdict(asset)
    self.assertEquals(countLaptops([asset]), 1)
