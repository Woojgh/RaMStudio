from django.urls import path
from .views import ShopView
from . import views

urlpatterns = [
    path('', views.ShopView, name='shop'),
]