from django.test import TestCase, RequestFactory
from ..companyusers.views import *
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company

class CompanyUserTest(TestCase):

  def test_get_queryset(self):
    user = User.objects.create(username='user1', password='12345', email='testuser@test.com', is_active=True)
    user.save()
    company = Company(name="Makers")
    company.save()
    CompanyUser.objects.create(user=user, company=company)
    request = RequestFactory().get('companyusers/api/companyusers/')
    view = CompanyUserList()
    request.user = user
    view.request = request
    qs = view.get_queryset()
    self.assertEqual(list(qs), list(CompanyUser.objects.all()))
