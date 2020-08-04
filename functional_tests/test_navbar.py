from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time

class NavBar(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_home_button(self):
    self.browser.get(self.live_server_url + '/login')
    home = self.browser.find_element_by_id('homeButton')
    home.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello world'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Hello world', body.text)

  def test_register_button(self):
    self.browser.get(self.live_server_url + '/login')
    register = self.browser.find_element_by_id('registerButton')
    register.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Register here'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('Password confirmation*', body.text)

  def test_login_button(self):
    self.browser.get(self.live_server_url)
    register = self.browser.find_element_by_id('id_login')
    register.send_keys(Keys.RETURN)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Login Here'))
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn("Don't have an account?", body.text)
