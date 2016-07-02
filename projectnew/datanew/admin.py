from django.contrib import admin

from models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

admin.site.register(Item,ItemAdmin)

