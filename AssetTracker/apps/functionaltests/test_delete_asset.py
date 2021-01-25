from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from ..assets.models import Asset
from ..companies.models import Company
from ..companyusers.models import CompanyUser
import time

class DeleteAssetTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(user=self.user, company=self.company)
    self.asset = Asset(asset_tag='BR20RL', device_type='laptop', created_by=self.user, company=self.company)
    self.asset.save()

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

  def test_delete_asset_and_does_not_display(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      asset_delete_button = self.browser.find_element_by_id('id_asset_delete_button_' + str(self.asset.id))
      asset_delete_button.send_keys(Keys.RETURN)
      confirm = self.browser.switch_to.alert
      confirm.accept()
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('BR20RL', body.text)

  def test_cancel_delete_asset_and_still_displays(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      asset_delete_button = self.browser.find_element_by_id('id_asset_delete_button_' + str(self.asset.id))
      asset_delete_button.send_keys(Keys.RETURN)
      confirm = self.browser.switch_to.alert
      confirm.dismiss()
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('BR20RL', body.text)
