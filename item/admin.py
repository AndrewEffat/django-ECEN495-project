from django.contrib import admin

# Register your models here.
from item.models import Item

admin.site.register(Item)