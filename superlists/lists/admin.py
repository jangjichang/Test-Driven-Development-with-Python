from django.contrib import admin
from lists.models import Item, List

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass
