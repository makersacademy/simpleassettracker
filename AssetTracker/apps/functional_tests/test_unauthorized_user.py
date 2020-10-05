from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from companies.models import Company
from companyusers.models import CompanyUser
from register.models import UnauthorizedUser
import time

class UnauthUserTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.company = Company(Name="Makers")
    self.company.save()
    self.admin = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.admin.save()
    self.company_user = CompanyUser.objects.create(User=self.admin, Company=self.company)
    self.user = User.objects.create_user(username='adam', password='adam1', email='adam@test.com', is_active=False)
    self.user.save()
    self.unauth_user = UnauthorizedUser.objects.create(User=self.user, Company=self.company)
    self.unauth_user.save()

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

  def test_page_loads(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/usermanagement/unauthorized')
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertIn('adam', body.text)

  def test_approve_user(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/usermanagement/unauthorized')
      time.sleep(1)
      user_approve_button = self.browser.find_element_by_id('id_user_approve_button_' + str(self.user.id))
      user_approve_button.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('adam', body.text)

  def test_deny_user(self):
    with self.settings(DEBUG=True):
      self.login()
      self.browser.get(self.live_server_url + '/usermanagement/unauthorized')
      time.sleep(1)
      user_deny_button = self.browser.find_element_by_id('id_user_deny_button_' + str(self.user.id))
      user_deny_button.send_keys(Keys.RETURN)
      time.sleep(1)
      body = self.browser.find_element_by_tag_name('body')
      self.assertNotIn('adam', body.text)
