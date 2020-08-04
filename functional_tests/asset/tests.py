from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time

class AssetTest(LiveServerTestCase):

  fixtures = ['functional_tests/fixtures/admin.json', 'functional_tests/fixtures/assets.json']

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_asset_display(self):
    self.browser.get('http://localhost:8000/assets/')
    body = self.browser.find_element(By.ID, 'app')
    self.assertIn('F22cvL', body.text)