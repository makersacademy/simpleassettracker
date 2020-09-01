from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from assets.models import Asset
import time

class AssetTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.user2 = User.objects.create_user(username='admin2', password='admin2', email='test2@test.com', is_active=True)
    self.user2.save()
    self.A = Asset(AssetTag='BR20RL', DeviceType='Laptop', CreatedBy=self.user)
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

  def login2(self):
    self.browser.get(self.live_server_url + '/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('admin2')
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys('admin2')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Your Dashboard'))

  def test_display_assets(self):  
    with self.settings(DEBUG=True):
        self.login()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Admin1', body.text)
        self.browser.get(self.live_server_url + '/assets')
        time.sleep(1)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('BR20RL', body.text)

  def test_asset_only_available_to_creator(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_tag_field = self.browser.find_element_by_id('id_add_asset_tag')
      asset_tag_field.send_keys('HD1269')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_type')
      asset_type_field.send_keys('Laptop')
      asset_submit_button = self.browser.find_element_by_id('id_add_asset_submit')
      asset_submit_button.send_keys(Keys.RETURN)
      logout = self.browser.find_element_by_id('id_navbar_logout')
      logout.send_keys(Keys.RETURN)
      self.login2()
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('HD1269', body.text)
