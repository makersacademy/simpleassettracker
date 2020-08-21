from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
import time

class NavBar(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()

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
  
  def test_home_button(self):
    self.browser.get(self.live_server_url + '/login')
    home = self.browser.find_element_by_id('id_navbar_home')
    home.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Index'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Index', body.text)

  def test_dashboard_button(self):
    self.login()
    self.browser.get(self.live_server_url + '/login')
    home = self.browser.find_element_by_id('id_navbar_home')
    home.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Your Dashboard'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Your Dashboard', body.text)

  def test_register_button(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/login')
      register = self.browser.find_element_by_id('id_navbar_register')
      register.send_keys(Keys.RETURN)
      wait = WebDriverWait(self.browser, 5)
      wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Register:'))
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Password confirmation*', body.text)

  def test_login_button(self):
    self.browser.get(self.live_server_url)
    login = self.browser.find_element_by_id('id_navbar_login')
    login.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Login:'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn("Don't have an account?", body.text)

  def test_asset_button(self):
    with self.settings(DEBUG=True):
      self.login()
      asset = self.browser.find_element_by_id('id_navbar_asset')
      asset.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn("Asset Tag", body.text)

  def test_import_button(self):
    with self.settings(DEBUG=True):
      self.login()
      upload = self.browser.find_element_by_id('id_navbar_import')
      upload.send_keys(Keys.RETURN)
      wait = WebDriverWait(self.browser, 5)
      wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Import Assets'))
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn("Import Assets", body.text)

  def test_add_asset_button(self):
    with self.settings(DEBUG=True):
      self.login()
      add_asset = self.browser.find_element_by_id('id_navbar_asset_add')
      add_asset.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn("Add an Asset", body.text)

  def test_asset_button_not_viewable_when_logged_out(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Assets', body.text)

  def test_add_asset_button_not_viewable_when_logged_out(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Add Asset', body.text)

  def test_logout_button_not_viewable_when_logged_out(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Log Out', body.text)

  def test_login_button_not_viewable_when_logged_in(self):
    self.login()
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Log In', body.text)

  def test_register_button_not_viewable_when_logged_in(self):
    self.login()
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Register', body.text)

  def test_import_button_not_viewable_when_logged_out(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('Import', body.text)
