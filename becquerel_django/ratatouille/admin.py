from django.contrib import admin

from .models import Ingredient, WebSite

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(WebSite)
