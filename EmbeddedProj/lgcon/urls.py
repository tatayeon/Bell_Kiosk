from django.urls import path, include
from . import views
from .views import payment_success

urlpatterns = [
   path('<int:pk>/', views.landing),
   path('test', views.test),
   path('payment-success/', payment_success, name='payment-success'),
]