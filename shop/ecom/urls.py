from django.urls import path
from . import views
from .views import ProductDetailView

urlpatterns = [
    # path("<str:name>", views.index, name="index"),
    path("healthcheck", views.health_check, name="health_check"),
    # ECOM URLS
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]