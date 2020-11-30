from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from ..companyusers.models import CompanyUser
from ..companies.models import Company
import time, sys, os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(os.path.sep, ROOT_DIR,'../../../static'+ os.sep)

class ImportcsvTest(LiveServerTestCase):

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

  def test_import_page_loads(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/import')
      body = self.browser.find_element_by_id('file_upload')
      assert 'File:' in body.text

  def test_csv_uploads(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/import')
      time.sleep(1)
      element = self.browser.find_element_by_id("csv_file")
      element.send_keys(csvpath+"static_csv/exampleasset.csv")
      button = self.browser.find_element_by_id("upload_button")
      button.send_keys(Keys.RETURN)
      time.sleep(1)
      self.browser.get(self.live_server_url + '/assets')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('TEST12', body.text)

  def test_invalid_file_type(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/import')
      time.sleep(1)
      element = self.browser.find_element_by_id("csv_file")
      element.send_keys(csvpath+"static_csv/invalidasset.txt")
      button = self.browser.find_element_by_id("upload_button")
      button.send_keys(Keys.RETURN)
      time.sleep(1)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('File is not CSV type', message.text)

  def test_invalid_file_format(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/import')
      time.sleep(1)
      element = self.browser.find_element_by_id("csv_file")
      element.send_keys(csvpath+"static_csv/invalidasset.csv")
      button = self.browser.find_element_by_id("upload_button")
      button.send_keys(Keys.RETURN)
      time.sleep(1)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Unable to upload file.', message.text)

  def test_empty_field_invalid(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/import')
      time.sleep(1)
      element = self.browser.find_element_by_id("csv_file")
      element.send_keys(csvpath+"static_csv/invalidasset.csv")
      button = self.browser.find_element_by_id("upload_button")
      button.send_keys(Keys.RETURN)
      time.sleep(1)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Field required - unable to upload.', message.text)
