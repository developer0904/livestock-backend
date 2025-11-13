from django.contrib import admin
from .models import InventoryItem


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity', 'unit', 'reorder_level', 'is_low_stock', 'total_value']
    list_filter = ['category', 'unit']
    search_fields = ['name', 'sku', 'supplier_name']
    readonly_fields = ['created_at', 'updated_at', 'is_low_stock', 'total_value']
