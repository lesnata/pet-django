from selenium import webdriver
from ecom.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
import time


class FunctionalTests(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.product_1 = Product.objects.create(name="Piano", price="505.00")

    def tearDown(self):
        self.browser.close()

    def test_store_page(self):
        self.browser.get(self.live_server_url)
        tag = self.browser.find_element_by_tag_name('h6')
        time.sleep(2)
        self.assertEquals(tag.text, self.product_1.name)

    def test_view_button_redirects_to_product_page(self):
        self.browser.get(self.live_server_url)
        product_url = self.live_server_url + reverse('product_detail', args=[self.product_1.id])
        time.sleep(3)
        self.browser.find_element_by_class_name('btn-outline-success').click()
        self.assertEquals(self.browser.current_url, product_url)

    def test_logged_user_checkout_page_empty_form(self):
        checkout_url = self.live_server_url + reverse('checkout')
        self.browser.get(checkout_url)
        time.sleep(3)
        hidden_element = self.browser.find_element_by_id('shipping-info').is_displayed()
        self.assertFalse(hidden_element)
