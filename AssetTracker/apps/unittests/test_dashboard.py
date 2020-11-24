from django.test import SimpleTestCase
from ..dashboard.views import countLaptops

class Dashboard(SimpleTestCase):

  def test_countLaptops_zero(self):
    assets = []
    self.assertEquals(countLaptops(assets), 0)

  def test_countLaptops_one(self):
    assets = ['Asset': {'device_type': 'Laptop'}]
    self.assertEquals(countLaptops(assets), 1)
