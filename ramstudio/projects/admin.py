from django.contrib import admin
from projects.models import Photo, Project


admin.site.register((Photo, Project))
