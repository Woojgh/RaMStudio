"""ramstudio URL Configuration"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('registration.backends.hmac.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('contact/', views.contact, name='contact'),
    path('grounds/', include('grounds.urls')),
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('shop/', include('shop.urls')),
    path('projects/', include('projects.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
