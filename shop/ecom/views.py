from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from . utils_ecom import cookieCart, cartData, guestOrder
from django.views.generic.detail import DetailView

# Create your views here


def health_check(request):
    return HttpResponse("OK")


#START


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('ProductId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    print('Product added:', product)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    print('Order number:', order)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    items = order.orderitem_set.all()
    print(f'What\'s inside our cart now?')
    for i in items:
        print(f'Product name: {i.product.name} \n'
              f'Product quantity: {i.quantity} \n'
              f'Product total: {i.get_total} \n'
              f'--------- Loading next ---------')

    return JsonResponse('Item was added', safe=False)


#@csrf_exempt
def processOrder(request):
    print(f'Data: {request.body}')
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    # creating Order model for authenticated and anonymous user
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()


# getting shipping data from front-end
    if order.shipping == True:
        # creating Shipping Address object
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment completed!', safe=False)


# TODO write view for product page
# def product_view(request, product_id):
#     print(f'Data: {request.body}')
#     data = cartData(request)
#     cartItems = data['cartItems']
#
#     product = Product.objects.get(id=product_id)
#     context = {'products': products, 'cartItems': cartItems}
#     return render(request, 'store.html', context)


class ProductDetailView(DetailView):
    model = Product
