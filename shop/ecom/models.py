from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Shop(models.Model):
    name = models.CharField('Name', max_lenght=255)
    city = models.CharField('City', max_lenght=255)
    # owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User',
                              on_delete=models.CASCADE)

    def __str__(self):
        return "%s shop by %s" % (self.name, self.owner)

# product itself
class Item(models.Model):
    title = models.CharField("Name", max_length=255, db_index=True)
    price = models.IntegerField("Price", max_length=20)
    category = models.CharField("Category", max_length=255, blank=True, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField("Photo", upload_to='images/%Y/%m/%d', help_text='Photo of Product', blank=True)
    in_stock = models.BooleanField()

    def __str__(self):
        return "%s in %s" % (self.name, self.shop)

#TODO
#class Buyer(models.Model):
#    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#    email = models.
#
#    def __str__(self):
#        return self.name


# intermediary step between  Item and Oder (product cart)
class OrderItem(models.Model):
    pass


class Order(models.Model):
    pass



