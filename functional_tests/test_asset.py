from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from assets.models import Asset
import time

class AssetTest(LiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.user = User.objects.create_user(username='admin1', password='admin1', email='test@test.com', is_active=True)
    self.user.save()
    self.A = Asset(AssetTag='BR20RL', DeviceType='Laptop', CreatedBy=self.user)
    self.A.save()

  def tearDown(self):
    self.browser.quit()

  def login(self):
    self.browser.get(self.live_server_url + '/login')
    username_field = self.browser.find_element_by_id('id_username')
    username_field.send_keys('admin1')
    print(1)
    password_field = self.browser.find_element_by_id('id_password')
    password_field.send_keys('admin1')
    password_field.send_keys(Keys.RETURN)
    print(2)
    wait = WebDriverWait(self.browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.ID, "content"), 'Hello'))

  def test_display_assets(self):
    self.login()
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('admin1', body.text)
    print(3)
    self.browser.get(self.live_server_url + '/assets')
    # Asset = self.browser.find_element_by_id('id_asset')
    # Asset.send_keys(Keys.RETURN)
    print(4)
    time.sleep(1)
    body = self.browser.find_element_by_tag_name('body')
    self.assertIn('BR20RL', body.text)

