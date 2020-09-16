from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time

class PreRegisterOptionsTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_page_loads(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/preregister')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Registration Options:', body.text)
      self.assertIn('Create A Workspace and Superuser', body.text)
      self.assertIn('Sign-In to an Existing Workspace', body.text)

  def test_navigate_to_register_company_page(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/preregister')
      company_button = self.browser.find_element_by_id('company_button')
      company_button.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Register A New Company and User:', body.text)

  def test_navigate_to_register_user_page(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/preregister')
      user_button = self.browser.find_element_by_id('user_button')
      user_button.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Register A New User:', body.text)
