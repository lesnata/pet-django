from django.test import TestCase, Client
from ecom.models import Customer, Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_1 = User.objects.create_user('karl', 'm@email.com', 'chevyspass')
        self.customer_1 = Customer.objects.create(user=self.user_1, name="Karl", email="m@email.com")
        self.product_1 = Product.objects.create(name="Pen", price="5.00")
        self.order_1 = Order.objects.create(customer=self.customer_1, transaction_id=1)
        self.order_item_1 = OrderItem.objects.create(product=self.product_1, order=self.order_1, quantity=2)
        self.shipping = ShippingAddress.objects.create(customer=self.customer_1,
                                                          order=self.order_1,
                                                          address='New hill street 9',
                                                          city='Denver',
                                                          state='WA',
                                                          zipcode='56874')

    def test_customer(self):
        pass

    def test_product_imageUrl(self):
        print('self.product_1.imageURL')
        print(self.product_1.imageURL)
        self.assertEqual(self.product_1.imageURL, '')

    def test_order_shipping(self):
        self.assertTrue(self.order_1.shipping)

    def test_order_get_cart_total(self):
        self.assertEqual(self.order_1.get_cart_total, '10.00')

    def test_order_get_cart_items(self):
        self.assertEqual(self.order_1.get_cart_items, 2)

    def test_orderItem_get_total(self):
        self.assertEqual(self.order_item_1.get_total, 2)



