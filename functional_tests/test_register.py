from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from companies.models import Company
from companyusers.models import CompanyUser
import time

class SignUpFormTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_company_form_exists(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registercompany')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Register A New Company and User:', body.text)
      self.assertIn('Company Name', body.text)
      self.assertIn('Username', body.text)
      self.assertIn('Password', body.text)
      self.assertIn('Email', body.text)
      self.assertIn('Password confirmation', body.text)

  def test_user_form_exists(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registeruser')
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('Register A New User:', body.text)
      self.assertIn('Company Name', body.text)
      self.assertIn('Username', body.text)
      self.assertIn('Password', body.text)
      self.assertIn('Email', body.text)
      self.assertIn('Password confirmation', body.text)

class SignUpUserAndCompanyTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_user_can_signup_a_new_company(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registercompany')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('Th1sIsAT3st.')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('Th1sIsAT3st.')
      password_field.send_keys(Keys.RETURN)
      time.sleep(2)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Your account and company has been created! Please sign in', message.text)

  def test_too_obvious_password(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registercompany')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('password')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('password')
      password_field.send_keys(Keys.RETURN)
      time.sleep(2)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Invalid form submission', message.text)

  def test_passwords_not_the_same(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registercompany')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('Th1sIsAT3st.')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('password')
      password_field.send_keys(Keys.RETURN)
      time.sleep(2)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Invalid form submission', message.text)

class SignUpUserTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(Name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(User=self.user, Company=self.company)

  def tearDown(self):
    self.browser.quit()

  def test_user_can_signup_to_a_company(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registeruser')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('Th1sIsAT3st.')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('Th1sIsAT3st.')
      password_field.send_keys(Keys.RETURN)
      time.sleep(2)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Your account has been created! Please sign in', message.text)

  def test_too_obvious_password(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registeruser')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('password')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('password')
      password_field.send_keys(Keys.RETURN)
      time.sleep(1)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Invalid form submission', message.text)

  def test_passwords_not_the_same(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/registeruser')
      name_field = self.browser.find_element_by_id('id_Name')
      name_field.send_keys('Makers')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('adam')
      email_field = self.browser.find_element_by_id('id_email')
      email_field.send_keys('adam@example.com')
      password_field = self.browser.find_element_by_id('id_password1')
      password_field.send_keys('Th1sIsAT3st.')
      password_confirmation_field = self.browser.find_element_by_id('id_password2')
      password_confirmation_field.send_keys('password')
      password_field.send_keys(Keys.RETURN)
      time.sleep(1)
      message = self.browser.find_element_by_class_name('messages')
      self.assertIn('Invalid form submission', message.text)

class LoginAndOutTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(Name="Makers")
    self.company.save()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.company_user = CompanyUser.objects.create(User=self.user, Company=self.company)

  def tearDown(self):
    self.browser.quit()

  def test_user_can_login_and_logout(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url + '/login')
      username_field = self.browser.find_element_by_id('id_username')
      username_field.send_keys('admin1')
      password_field = self.browser.find_element_by_id('id_password')
      password_field.send_keys('admin1')
      password_field.send_keys(Keys.RETURN)
      wait = WebDriverWait(self.browser, 5)
      wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Your Dashboard'))
      body = self.browser.find_element_by_tag_name('body')

      self.assertIn('Admin1', body.text)
      logout = self.browser.find_element_by_id('id_navbar_logout')
      logout.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('Admin1', body.text)
