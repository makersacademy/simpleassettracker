from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time

class AdminTest(LiveServerTestCase):

  fixtures = ['functional_tests/fixtures/admin.json']

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_admin_site(self):
    self.browser.get('http://localhost:8000/admin/')
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Django administration', body.text)
    username_field = self.browser.find_element_by_name('username')
    username_field.send_keys('admin')
    password_field = self.browser.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Site administration'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Site administration', body.text)

class SignUpFormTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_form_exists(self):
    self.browser.get('http://localhost:8000/register/')
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Username', body.text)
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Password', body.text)
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Email', body.text)
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Password confirmation', body.text)

class SignUpTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_user_can_signup(self):
    self.browser.get('http://localhost:8000/register/')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('adam')
    email_field = self.browser.find_element_by_id('id_email')
    email_field.send_keys('adam@gmail.com')
    password_field = self.browser.find_element_by_id('id_password1')
    password_field.send_keys('password')
    password_confirmation_field = self.browser.find_element_by_id('id_password2')
    password_confirmation_field.send_keys('password')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Hello', body.text)

class LoginAndOutTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_user_can_login_and_logout(self):
    # loggin in
    self.browser.get('http://localhost:8000/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('admin')
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello'))
    body = self.browser.find_element_by_tag_name('body')

    self.assertIn('admin', body.text)
    logout = self.browser.find_element_by_id('id_logout')
    logout.send_keys(Keys.RETURN)
    time.sleep(1)
    # wait = WebDriverWait(self.browser, 1)
    # wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'hello'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('admin', body.text)

class IndexTest(LiveServerTestCase):
  def test_hello_world(self):
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000/')

    body = browser.find_element_by_tag_name('body')
    assert 'Hello' in body.text

    browser.quit()
