from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'priceh', 'pricef')
    list_filter = ('category',)
    search_fields = ('name', 'category')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantityh', 'quantityf', 'order')
    list_filter = ('order',)

class ItemInline(admin.TabularInline):
    model = Item
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'type', 'amount', 'timestamp')
    list_filter = ('username', 'phone', 'type', 'timestamp')
    search_fields = ('username', 'phone', 'type', 'address', 'amount', 'timestamp')
    inlines = [ItemInline]
    readonly_fields = ('timestamp',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)