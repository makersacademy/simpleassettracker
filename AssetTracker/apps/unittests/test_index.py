from django.test import TestCase, Client
from ..index.views import indexPageView

class IndexTest(TestCase):

  def setUp(self):
    self.client = Client()

  def test_index_page_view(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index/index.html')
