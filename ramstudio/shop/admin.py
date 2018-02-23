from django.contrib import admin
from shop.models import Photo, Item, Cart


admin.site.register((Photo, Item, Cart))
