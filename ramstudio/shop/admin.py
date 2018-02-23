from django.contrib import admin
from shop.models import Photo, Item


admin.site.register((Photo, Item))
