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

class DashboardTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(user=self.user, company=self.company)

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

  def test_dashboard_not_viewable_when_logged_out(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/dashboard')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Login:', body.text)

  def test_zero_asset_count(self):
    with self.settings(DEBUG=True):
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 0', body.text)

  def test_dashboard_showing_count_of_assets(self):
    with self.settings(DEBUG=True):
      self.A = Asset(asset_tag='BR20RL', device_type='laptop', device_model='Air', asset_status='Ready', serial_number='57', created_by=self.user, company=self.company)
      self.A.save()
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 1', body.text)

  def test_dashboard_showing_count_of_laptops(self):
    with self.settings(DEBUG=True):
      self.A = Asset(asset_tag='BR20RL', device_type='laptop', device_model='Air', asset_status='Ready', serial_number='56', created_by=self.user, company=self.company)
      self.A.save()
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of laptops: 1', body.text)
      self.assertIn('Total number of mobiles: 0', body.text)

  def test_dashboard_showing_count_of_mobiles(self):
    with self.settings(DEBUG=True):
      self.A = Asset(asset_tag='BB23A', device_type='Mobile', device_model='iPhone 6', asset_status='Ready', imei='55', created_by=self.user, company=self.company)
      self.A.save()
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of laptops: 0', body.text)
      self.assertIn('Total number of mobiles: 1', body.text)

  def test_add_asset_and_count_increases(self):
    with self.settings(DEBUG=True):
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 0', body.text)
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_type_field = self.browser.find_element_by_id('id_select_asset_type')
      asset_type_field.send_keys('Laptop')
      asset_tag_field = self.browser.find_element_by_id('id_add_asset_tag')
      asset_tag_field.send_keys('HD1269')
      asset_type_field = self.browser.find_element_by_id('id_add_serial_number')
      asset_type_field.send_keys('7')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_status')
      asset_type_field.send_keys('Ready')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_model')
      asset_type_field.send_keys('Pro')
      asset_type_field = self.browser.find_element_by_id('id_add_asset_condition')
      asset_type_field.send_keys('Good')
      asset_type_field = self.browser.find_element_by_id('id_add_year')
      asset_type_field.send_keys('2013')
      asset_type_field = self.browser.find_element_by_id('id_add_ram')
      asset_type_field.send_keys('8GB')
      asset_type_field = self.browser.find_element_by_id('id_add_screen_size')
      asset_type_field.send_keys('16 inches')
      asset_type_field = self.browser.find_element_by_id('id_add_hard_drive')
      asset_type_field.send_keys('256GB')
      asset_submit_button = self.browser.find_element_by_id('id_add_asset_submit')
      asset_submit_button.send_keys(Keys.RETURN)
      time.sleep(1)
      self.browser.get(self.live_server_url + '/dashboard')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 1', body.text)

  def test_asset_deletes_and_count_decreases(self):
    with self.settings(DEBUG=True):
      self.A = Asset(asset_tag='BB23A', device_type='mobile', device_model='iPhone 6', asset_status='Ready', imei='58', created_by=self.user, company=self.company)
      self.A.save()
      self.login()
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 1', body.text)
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      asset_delete_button = self.browser.find_element_by_id('id_asset_delete_button_' + str(self.A.id))
      asset_delete_button.send_keys(Keys.RETURN)
      confirm = self.browser.switch_to.alert
      confirm.accept()
      time.sleep(1)
      self.browser.get(self.live_server_url + '/dashboard')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Total number of assets: 0', body.text)
