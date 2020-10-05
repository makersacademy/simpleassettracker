from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from AssetTracker.apps.assets.models import Asset
from AssetTracker.apps.companies.models import Company
from AssetTracker.apps.companyusers.models import CompanyUser
import time

class AssetTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(Name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(User=self.user, Company=self.company)
    self.company2 = Company(Name="IBM")
    self.company2.save()
    self.user2 = User.objects.create_user(username='admin2', password='admin2', email='test2@test.com', is_active=True)
    self.user2.save()
    self.company_user2 = CompanyUser.objects.create(User=self.user2, Company=self.company2)
    self.user3 = User.objects.create_user(username='admin3', password='admin3', email='test3@test.com', is_active=True)
    self.user3.save()
    self.company_user3 = CompanyUser.objects.create(User=self.user3, Company=self.company)
    self.A = Asset(AssetTag='BR20RL', DeviceType='Laptop', AssetStatus='Ready', SerialNumber='6', CreatedBy=self.user, Company=self.company)
    self.A.save()

  def tearDown(self):
    self.browser.quit()

  def login(self, username, password):
    self.browser.get(self.live_server_url + '/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys(username)
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Your Dashboard'))

  def test_display_assets(self):
    with self.settings(DEBUG=True):
      self.login('admin1', 'admin1')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Admin1', body.text)
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(3)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('BR20RL', body.text)

  def test_asset_visible_to_different_users_from_same_company(self):
    with self.settings(DEBUG=True):
      self.login('admin1', 'admin1')
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_tag_field = self.browser.find_element_by_id('id_add_asset_tag')
      asset_tag_field.send_keys('HD1269')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_type')
      asset_type_field.send_keys('Laptop')
      asset_type_field = self.browser.find_element_by_id('id_add_serial_number')
      asset_type_field.send_keys('5')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_status')
      asset_type_field.send_keys('Ready')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_model')
      asset_type_field.send_keys('Pro')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_condition')
      asset_type_field.send_keys('Good')
      asset_type_field = self.browser.find_element_by_id('id_add_year')
      asset_type_field.send_keys('2013')
      asset_type_field = self.browser.find_element_by_id('id_add_ram')
      asset_type_field.send_keys('8')
      asset_type_field = self.browser.find_element_by_id('id_add_screen_size')
      asset_type_field.send_keys('18')
      asset_type_field = self.browser.find_element_by_id('id_add_hard_drive')
      asset_type_field.send_keys('256')
      asset_submit_button = self.browser.find_element_by_id('id_add_asset_submit')
      asset_submit_button.send_keys(Keys.RETURN)
      logout = self.browser.find_element_by_id('id_navbar_logout')
      logout.send_keys(Keys.RETURN)
      self.login('admin3', 'admin3')
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(5)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('HD1269', body.text)

  def test_asset_not_available_to_user_from_different_company(self):
    with self.settings(DEBUG=True):
      self.login('admin1', 'admin1')
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_tag_field = self.browser.find_element_by_id('id_add_asset_tag')
      asset_tag_field.send_keys('HD1269')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_type')
      asset_type_field.send_keys('Laptop')
      asset_type_field = self.browser.find_element_by_id('id_add_serial_number')
      asset_type_field.send_keys('5')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_status')
      asset_type_field.send_keys('Ready')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_model')
      asset_type_field.send_keys('Pro')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_condition')
      asset_type_field.send_keys('Good')
      asset_type_field = self.browser.find_element_by_id('id_add_year')
      asset_type_field.send_keys('2013')
      asset_type_field = self.browser.find_element_by_id('id_add_ram')
      asset_type_field.send_keys('8')
      asset_type_field = self.browser.find_element_by_id('id_add_screen_size')
      asset_type_field.send_keys('18')
      asset_type_field = self.browser.find_element_by_id('id_add_hard_drive')
      asset_type_field.send_keys('256')
      asset_submit_button = self.browser.find_element_by_id('id_add_asset_submit')
      asset_submit_button.send_keys(Keys.RETURN)
      logout = self.browser.find_element_by_id('id_navbar_logout')
      logout.send_keys(Keys.RETURN)
      self.login('admin2', 'admin2')
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('HD1269', body.text)
      self.assertNotIn('BR20RL', body.text)
