from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    # Value which shows in our admin panel
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Product could be digital - non-shipping or physical with delivery. By default = physical
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    # Many-To-Many: customer has muplitple orders. if customer is deleted, customer in order sets to Null
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        # converting to string, can't return integer
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        # getting all child objects of Parent obj (self.)
        orderitems = self.orderitem_set.all()
        # item.get_total - обращаемся к созданному атрибуту в прошлом классе
        # Orderitem в каждом обьекте списка OrderItems
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
















# class Shop(models.Model):
#     name = models.CharField('Name', max_lenght=255)
#     city = models.CharField('City', max_lenght=255)
#     # owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     owner = models.ForeignKey('auth.User',
#                               on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s shop by %s" % (self.name, self.owner)
#
# # product itself
# class Item(models.Model):
#     title = models.CharField("Name", max_length=255, db_index=True)
#     price = models.IntegerField("Price", max_length=20)
#     category = models.CharField("Category", max_length=255, blank=True, null=True)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField("Photo", upload_to='images/%Y/%m/%d', help_text='Photo of Product', blank=True)
#     in_stock = models.BooleanField()
#
#     def __str__(self):
#         return "%s in %s" % (self.name, self.shop)

#TODO
#class Buyer(models.Model):
#    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    email = models.
#
#    def __str__(self):
#        return self.name



