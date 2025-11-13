from django.contrib import admin
from .models import Owner


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'farm_name', 'city', 'state', 'is_active']
    list_filter = ['is_active', 'state', 'city']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'farm_name']
    readonly_fields = ['created_at', 'updated_at']
