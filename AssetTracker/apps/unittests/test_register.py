from django.test import TestCase, Client
from ..register.views import preregisterview

class PreRegisterTest(TestCase):

  def setUp(self):
    self.client = Client()

  def test_preregister_page_view(self):
    response = self.client.get('/preregister', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'register/preregister.html')

class RegisterCompanyTest(TestCase):

  def setUp(self):
    self.client = Client()

  def test_register_company_page_view(self):
    response = self.client.get('/registercompany', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'register/registercompany.html')
