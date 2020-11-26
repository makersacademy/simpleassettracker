from django.test import TestCase, Client
from ..reactfrontend.views import *

class Reactfrontend(TestCase):
  def setUp(self):
    self.client = Client()

  def test_assets(self):
    response = self.client.get('/assets')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/assets.html')
    self.assertContains(response, 'Your Assets')

  def test_addAssets(self):
    response = self.client.get('/assets/add')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/addAssets.html')
    self.assertContains(response, 'Add an Asset')

  def test_unauthorizedUsers(self):
    response = self.client.get('/usermanagement/unauthorized')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/unauthorizedUsers.html')
    self.assertContains(response, 'Unauthorized Users')
