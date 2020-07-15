from django.test import TestCase
from models import test_method

# models test
class ModelsTest(TestCase):
  def test(self):
    num = 10
    outcome = test_method(num)
    self.assertEqual(outcome, 15)

