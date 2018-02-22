from django.urls import path
from .views import GroundsView, GroundsShopView
from . import views

urlpatterns = [
    path('', views.GroundsView, name='grounds'),
    path('shop/', views.GroundsShopView, name='grounds-shop'),
]