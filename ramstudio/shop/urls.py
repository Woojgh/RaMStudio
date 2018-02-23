from django.urls import path
from .views import ShopView, ShopCreateView, ShopDetailView, ShoppingCart

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', ShoppingCart.as_view(), name='shopping_cart'),
    path('item_create/', ShopCreateView.as_view(), name='item_create'),
    path('item_detail/<int:id>/', ShopDetailView.as_view(), name='item_detail'),
]