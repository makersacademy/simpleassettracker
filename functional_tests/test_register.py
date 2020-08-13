import time

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SignUpFormTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_form_exists(self):
    self.browser.get(self.live_server_url + '/register')
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
    self.browser.get(self.live_server_url + '/register')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('adam')
    email_field = self.browser.find_element_by_id('id_email')
    email_field.send_keys('adam@example.com')
    password_field = self.browser.find_element_by_id('id_password1')
    password_field.send_keys('Th1sIsAT3st.')
    password_confirmation_field = self.browser.find_element_by_id('id_password2')
    password_confirmation_field.send_keys('Th1sIsAT3st.')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Hello', body.text)


class LoginAndOutTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()

  def tearDown(self):
    self.browser.quit()

  def test_user_can_login_and_logout(self):
    # loggin in
    self.browser.get(self.live_server_url + '/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('admin1')
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys('admin1')
    password_field.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello world'))
    body = self.browser.find_element_by_tag_name('body')

    self.assertIn('admin1', body.text)
    logout = self.browser.find_element_by_id('id_navbar_logout')
    logout.send_keys(Keys.RETURN)
    time.sleep(1)
    body = self.browser.find_element_by_tag_name('body')
    self.assertNotIn('admin1', body.text)


class IndexTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_hello_world(self):
    self.browser.get(self.live_server_url)
    body = self.browser.find_element_by_tag_name('body')
    assert 'Hello' in body.text
