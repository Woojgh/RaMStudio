from django.urls import path
from .views import GroundsView
from . import views

urlpatterns = [
    path('', views.GroundsView, name='grounds'),
]