from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse, resolve
from ecom.views import store, cart, checkout, ProductDetailView, updateItem, processOrder
from ecom.models import Customer, Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User
import json

# TODO Views test-case

class TestViews(TestCase):

    def setUp(self):
        # Setting up urls
        self.store_url = reverse('store')
        self.cart_url = reverse('cart')
        self.checkout_url = reverse('checkout')
        self.update_item = reverse('update_item')
        self.product_detail_url = reverse('product_detail', args=[1])

        # Setting up objects
        self.client = Client()
        self.user_1 = User.objects.create_user('karl', 'm@email.com', 'chevyspass')
        self.customer_1 = Customer.objects.create(user=self.user_1, name="Karl", email="m@email.com")
        self.product_1 = Product.objects.create(name="Pen", price="5.00")
        self.order_1 = Order.objects.create(customer=self.customer_1, transaction_id=1)
        self.order_item_1 = OrderItem.objects.create(product=self.product_1, order=self.order_1, quantity=2)

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

    def test_updateItem_order_is_created(self):
        last_order = Order.objects.latest('id')
        print("Id of last created Order is:")
        print(last_order.id)
        self.assertEqual(self.order_1.id, last_order.id)

    def test_updateItem_orderItem_is_created(self):
        last_order_item = OrderItem.objects.latest('id')
        self.assertEqual(self.order_item_1.id, last_order_item.id)

    def test_updateItem_action_add(self):
        self.client.login(username='karl', password='chevyspass')
        request_1 = {'productId': self.product_1.id, 'action': 'add'}
        response = self.client.post(reverse('update_item'), json.dumps(request_1), content_type='application/json')
        updated_order_item = OrderItem.objects.get(id=self.product_1.id)
        print('Updated order item quantity:')
        print(updated_order_item.quantity)
        self.assertEqual(updated_order_item.quantity, 3)
        self.assertEqual(response.status_code, HTTPStatus.OK)


        # Request: < WSGIRequest: POST '/update_item/' >
        # Request type: <class 'django.core.handlers.wsgi.WSGIRequest'>
        #
        # --------------------------------------
        # Json.loads(request.body) is:
        # {'productId': '1', 'action': 'add'}

        # request.user: admin_lesna
        # request.user.customer: Natalie



        #response = self.client.get(reverse('update_item'), json.loads(data))

        # Data: b'{"form":{"name":null,"email":null,"total":"82.50"},"shipping":{"address":"Sezame street","city":"Adelaide","state":"WU","zipcode":"065555"}}'
        #
        # Data: b'{"form":{"name":"testing","email":"sd@email.com","total":"53.30"},"shipping":{"address":"Sezame street","city":"Adelaide","state":"AW","zipcode":"3066"}}'
        # Data: < WSGIRequest: POST
        # '/process_order/' >
        # Data: <
        #
        # class 'django.core.handlers.wsgi.WSGIRequest'>

        #self.assertRedirects(response, "/thanks/")




# TODO ProcessOrder test
    # def test_processOrder(self):
    #
    #     self.assertEqual(processOrder(fooo), JsonResponse('Payment completed!', safe=False))



# TODO ProductDetail class based view
#     def test_product_detail_GET(self):
#         response = self.client.get(self.product_detail_url)
#         print("Here is what's in Response")
#         print(response)
#         self.assertEqual(1, 1)
#         self.assertEqual(context, product_1.name)


        # url = reverse('product_detail', args=[1])
        #
        # #response = self.client.get(self.product_detail_url)
        #
        # self.assertEqual(resolve(url).func.view_class, HTTPStatus.OK)



#         url = reverse('product_detail', args=[1])
#         print(url)
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, ProductDetailView)
#
#
#response = self.client.get(reverse('gene:person-list'))
       # self.assertIn('environment', response.context)
#
#
# import unittest
# from django.test import Client
#
# class SimpleTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#         person1 = Person.objects.create(name="Person 1")
#         person2 = Person.objects.create(name="Person 2")
#
#     def test_details(self):
#         response = self.client.get(reverse('gene:person-list'))
#         self.assertIn('environment', response.context)
