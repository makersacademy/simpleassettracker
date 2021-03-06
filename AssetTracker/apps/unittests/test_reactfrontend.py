from django.test import TestCase, Client
from ..reactfrontend.views import *
from django.contrib.auth.models import User

class ReactfrontendTest(TestCase):
  
  def setUp(self):
    self.client = Client()
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    self.client.login(username='testuser', password='12345')

  def test_assets_page_view(self):
    response = self.client.get('/assets', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/assets.html')

  def test_add_assets_page_view(self):
    response = self.client.get('/assets/add')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/addAssets.html')

  def test_unauthorized_users_page_view(self):
    response = self.client.get('/usermanagement/unauthorized')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/unauthorizedUsers.html')
  
  def test_importcsv_page_view(self):
    response = self.client.get('/import', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'reactfrontend/importcsv.html')
