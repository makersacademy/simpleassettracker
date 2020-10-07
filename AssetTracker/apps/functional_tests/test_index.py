from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test import LiveServerTestCase
import time

class IndexTest(LiveServerTestCase):
  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_index_text(self):
    with self.settings(DEBUG=True):
      self.browser.get(self.live_server_url)
      body = self.browser.find_element_by_tag_name('body')
      assert 'Simple Asset Tracker' in body.text
