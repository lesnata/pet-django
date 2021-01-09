from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ecom.views import store, cart, checkout, ProductDetailView, updateItem, processOrder


class TestUrls(SimpleTestCase):

    def test_store_url_resolves(self):
        url = reverse('store')
        self.assertEquals(resolve(url).func, store)

    def test_cart_url_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)

    def test_checkout_url_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_update_item_url_resolves(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func, updateItem)

    def test_process_order_url_resolves(self):
        url = reverse('process_order')
        self.assertEquals(resolve(url).func, processOrder)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProductDetailView)


# TODO Function tests


