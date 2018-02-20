from django.urls import path
from .views import emailView, successView
from . import views

urlpatterns = [
    path('', views.emailView, name='contact-email'),
    path('success/', views.successView, name='contact-success'),
]