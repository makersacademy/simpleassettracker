from django.test import TestCase, Client, RequestFactory
from ..companyusers.views import *
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company

class CompanyUser(TestCase):

  def setUp(self):
    self.client = Client()
    user = User.objects.create(username='user1')
    user.set_password('12345')
    user.save()
    company = Company(name="Makers")
    company.save()
    CompanyUser.objects.create(user=user, company=company)

  def test_get_queryset(self):
    request = RequestFactory().get('companyusers/api/companyusers/')
    view = CompanyUserList()
    view.request = request
    qs = view.get_queryset()
    self.assertQuerysetEqual(qs, CompanyUser.objects.all())
