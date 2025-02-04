from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category',CategoryDetails,basename="category")
router.register(r'product',ProductDetails,basename="product")
router.register(r'stock',StockDetails,basename="stock")
router.register(r'order',OrderDetails,basename="order")
router.register(r'orderitem',OrderItemDetails,basename="orderitem")
router.register(r'payment',PaymentDetails,basename="payment")


urlpatterns = [
    path('',include(router.urls))
]
