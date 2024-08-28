# orders/urls.py
from django.urls import path
from .views import OrderDataAPIView
from .views import order_list_view

urlpatterns = [
    path('api/order-data/', OrderDataAPIView.as_view(), name='order-data'),
    path('orders/', order_list_view, name='order-list'),
]
