from django.test import TestCase, Client, RequestFactory
from ..register.views import *
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company

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

class UnauthorizedUserTest(TestCase):

  def setUp(self):
    user = User.objects.create(username='user1', password='12345', email='testuser@test.com', is_active=True)
    user.save()
    company = Company(name="Makers")
    company.save()
    CompanyUser.objects.create(user=user, company=company)

  def test_get_queryset(self):
    user = User.objects.get(username='user1')
    unauth_user = User.objects.create(username='unauth user', password='56789', email='unauthuser@test.com', is_active=False)
    unauth_user.save()
    unauth_user_company = Company.objects.get(name="Makers")
    UnauthorizedUser.objects.create(user=user, company=unauth_user_company)
    request = RequestFactory().get('unauthorizedusers/api/unauthorizedusers')
    view = UnauthorizedUserList()
    request.user = user
    view.request = request
    qs = view.get_queryset()
    self.assertEqual(list(qs), list(UnauthorizedUser.objects.all()))
