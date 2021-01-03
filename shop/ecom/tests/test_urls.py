from django.test import TestCase
from django.urls import reverse, resolve


#FIXTURES = ['']

# TODO Models test-case: creation, save, remove
# TODO Views test-case:
# TODO URLS test
# TODO Function tests

class TestUrls:

    def test_product_detail_url(self):
        path = reverse('store')
        assert resolve(path).view_name == 'store'




# class TestView(TestCase):
#     fixtures = FIXTURES
#
#     def test_customer(self):
#         response = self.client.get(reverse('customer'))
#         self.assertEqual(response.status_code, 200)
#
#     def test_product(self):
#         response = self.client.get(reverse('product'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'ecom/product_detail.html')
#
#     def test_order(self):
#         response = self.client.get(reverse('order'))
#
