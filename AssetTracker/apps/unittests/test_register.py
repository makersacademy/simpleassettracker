from django.test import TestCase, Client
from ..register.views import pre_register_view, register_company, register_user

class PreRegisterTest(TestCase):

  def setUp(self):
    self.client = Client()

  def test_pre_register_page_view(self):
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

class RegisterUserTest(TestCase):

  def setUp(self):
    self.client = Client()

  def test_register_user_page_view(self):
    response = self.client.get('/registeruser', follow=True)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'register/registeruser.html')
