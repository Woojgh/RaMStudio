from django.urls import path
from .views import GroundsView, GroundsShopView, GroundsDeckView, GroundsFirepitView, GroundsFrontView, GroundsGreenhouseView, GroundsHastaView, GroundsMeditationView, GroundsPondView, GroundsZenView
from . import views

urlpatterns = [
    path('', views.GroundsView, name='grounds'),
    path('deck/', views.GroundsDeckView, name='grounds-deck'),
    path('firepit/', views.GroundsFirepitView, name='grounds-firepit'),
    path('front/', views.GroundsFrontView, name='grounds-front'),
    path('greenhouse/', views.GroundsGreenhouseView, name='grounds-greenhouse'),
    path('hasta/', views.GroundsHastaView, name='grounds-hasta'),
    path('meditation/', views.GroundsMeditationView, name='grounds-meditation'),
    path('pond/', views.GroundsPondView, name='grounds-pond'),
    path('shop/', views.GroundsShopView, name='grounds-shop'),
    path('zen/', views.GroundsZenView, name='grounds-zen'),
]