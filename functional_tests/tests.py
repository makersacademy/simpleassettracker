from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase

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

class SignUpTest(LiveServerTestCase):

  def test_form_exists(self):
    self.browser.get('http://localhost:8000/register/')
    body = self.browser.find_element_by_tag_name('body')

# class IndexTest(LiveServerTestCase):
#   def test_hello_world(self):
#     browser = webdriver.Firefox()
#     browser.get('http://localhost:8000/')

#     body = browser.find_element_by_tag_name('body')
#     assert 'Hello World!' in body.text

#     browser.quit()
