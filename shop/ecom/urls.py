from django.urls import path
from . import views

urlpatterns = [
    # path("<str:name>", views.index, name="index"),
    path("test", views.test, name="test"),
    path("add", views.add, name="add"),
    path("index", views.index, name="index"),
    path("healthcheck", views.health_check, name="health_check"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("product/<slug>/", views.product, name="product"),
    path("add_shop", views.add_shop, name="add_shop"),
    path("add_product", views.add_product, name="add_product"),
]
