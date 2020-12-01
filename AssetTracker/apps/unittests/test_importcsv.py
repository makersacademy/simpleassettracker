from django.test import TestCase, Client
from ..importcsv.views import importView
from django.contrib.auth.models import User

class ImportCSVTest(TestCase):

  def setUp(self):
    self.client = Client()
    user = User.objects.create(username='testuser')
    user.set_password('12345')
    user.save()
    self.client.login(username='testuser', password='12345')

  def test_importcsv_page_view(self):
    response = self.client.get('/import', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'importcsv/importcsv.html')
