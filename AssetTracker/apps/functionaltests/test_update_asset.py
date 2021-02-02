from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company
from ..assets.models import Asset
import time

class AssetUpdateTest(LiveServerTestCase):
  
  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(user=self.user, company=self.company)
    self.A = Asset(asset_tag='BR20RL', asset_status='Ready', serial_number='6', device_type='Laptop', created_by=self.user, company=self.company)
    self.A.save()

  def tearDown(self):
    self.browser.quit()

  def login(self):
    self.browser.get(self.live_server_url + '/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('admin1')
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys('admin1')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Your Dashboard'))

  def test_display_single_asset(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      self.browser.find_element_by_id('tagid').click()
      select = Select(self.browser.find_element_by_id('id_add_asset_status'))
      select.select_by_visible_text('Lost')
      self.browser.find_element_by_id('single-asset-submit').click()
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Lost', body.text)
