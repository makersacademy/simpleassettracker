from django.test import SimpleTestCase
from ..dashboard.views import countLaptops

class Dashboard(SimpleTestCase):

  def test_countLaptops(self):
    assets = []
    self.assertEquals(countLaptops(assets), 0)
