from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from ..companies.models import Company
from ..companyusers.models import CompanyUser
import time

class AddAssetTest(LiveServerTestCase):

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

  def test_add_asset_on_page(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Add an Asset', body.text)

  def test_select_an_asset_form_is_on_page(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_select_field = self.browser.find_element_by_id('id_select_asset_type')
      self.assertEquals(True, asset_select_field.is_displayed())

  def test_laptop_form_can_be_submitted_and_redirect(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/assets/add')
      time.sleep(1)
      asset_type_field = self.browser.find_element_by_id('id_select_asset_type')
      asset_type_field.send_keys('Laptop')
      asset_tag_field = self.browser.find_element_by_id('id_add_asset_tag')
      asset_tag_field.send_keys('HD1269')
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
      asset_type_field.send_keys('8GB')
      asset_type_field = self.browser.find_element_by_id('id_add_screen_size')
      asset_type_field.send_keys('16 inches')
      asset_type_field = self.browser.find_element_by_id('id_add_hard_drive')
      asset_type_field.send_keys('256GB')
      asset_submit_button = self.browser.find_element_by_id('id_add_asset_submit')
      asset_submit_button.send_keys(Keys.RETURN)
      time.sleep(1)
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('HD1269', body.text)
