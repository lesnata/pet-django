from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse, resolve
from ecom.views import store, cart, checkout, ProductDetailView, updateItem, processOrder
from ecom.models import Customer, Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
import json


class TestViews(TestCase):

    def setUp(self):
        # Setting up urls
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        self.update_item = reverse('update_item')
        self.process_order = reverse('process_order')
        self.product_detail = reverse('product_detail', args=[1])

        # Setting up objects
        self.client = Client()
        self.user_1 = User.objects.create_user('karl', 'm@email.com', 'chevyspass')
        self.customer_1 = Customer.objects.create(user=self.user_1, name="Karl", email="m@email.com")
        self.product_1 = Product.objects.create(name="Pen", price="5.00")
        self.order_1 = Order.objects.create(customer=self.customer_1, transaction_id=1)
        self.order_item_1 = OrderItem.objects.create(product=self.product_1, order=self.order_1, quantity=2)

    def tearDown(self):
        self.user_1.delete()
        self.customer_1.delete()
        self.product_1.delete()
        self.order_1.delete()
        self.order_item_1.delete()

    def test_store_HTTPStatus(self):
        response = self.client.get(self.store_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'store.html')

    def test_cart_HTTPStatus(self):
        response = self.client.get(self.cart_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'cart.html')

    def test_checkout_HTTPStatus(self):
        response = self.client.get(self.checkout_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'checkout.html')


    def test_ProductDetail_template(self):
        response = self.client.get(self.product_detail)
        print("Response is in test_ProductDetail_template")
        print(response)
        self.assertTemplateUsed(response, 'product_detail.html')

    def test_ProductDetail_object_in_context(self):
        response = self.client.get(self.product_detail)
        self.assertEqual(response.context[0]['object'], Product.objects.get(id=1))
        #self.assertIn(Product.objects.get(id=1), response.context[0][3])



    def test_updateItem_order_is_created(self):
        last_order = Order.objects.latest('id')
        self.assertEqual(self.order_1.id, last_order.id)

    def test_updateItem_orderItem_is_created(self):
        last_order_item = OrderItem.objects.latest('id')
        self.assertEqual(self.order_item_1.id, last_order_item.id)

    def test_updateItem_action_add(self):
        self.client.login(username='karl', password='chevyspass')
        request_1 = {'productId': self.product_1.id, 'action': 'add'}
        response = self.client.post(self.update_item, json.dumps(request_1), content_type='application/json')
        updated_order_item = OrderItem.objects.get(id=self.product_1.id)
        self.assertEqual(updated_order_item.quantity, 3)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_updateItem_action_remove(self):
        self.client.login(username='karl', password='chevyspass')
        request_2 = {'productId': self.product_1.id, 'action': 'remove'}
        response = self.client.post(self.update_item, json.dumps(request_2), content_type='application/json')
        updated_order_item = OrderItem.objects.get(id=self.product_1.id)
        self.assertEqual(updated_order_item.quantity, 1)

    def test_updateItem_deletion(self):
        self.client.login(username='karl', password='chevyspass')
        request_3 = {'productId': self.product_1.id, 'action': 'remove'}
        response = self.client.post(self.update_item, json.dumps(request_3), content_type='application/json')
        response = self.client.post(self.update_item, json.dumps(request_3), content_type='application/json')
        with self.assertRaises(OrderItem.DoesNotExist):
            OrderItem.objects.get(id=self.product_1.id)

    def test_processOrder_order_completed(self):
        self.client.login(username='karl', password='chevyspass')
        product_2 = Product.objects.create(name="Candy", price="10.0")
        order_item_2 = OrderItem.objects.create(product=product_2, order=self.order_1, quantity=1)
        user_form_data = {
            'form': {
                'total': '20.00'
            },
            'shipping': {
                    'address': 'Old school street 9',
                    'city': 'Rolls-Royce',
                    'state': 'KU',
                    'zipcode': '12355',
                }
            }

        response = self.client.post(self.process_order, json.dumps(user_form_data), content_type='application/json')
        updated_order = Order.objects.get(id=self.customer_1.id)
        self.assertTrue(updated_order.complete)




