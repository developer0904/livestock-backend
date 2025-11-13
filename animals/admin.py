from django.contrib import admin
from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['tag_id', 'name', 'species', 'breed', 'gender', 'status', 'owner', 'created_at']
    list_filter = ['species', 'gender', 'status', 'owner']
    search_fields = ['tag_id', 'name', 'breed', 'owner__first_name', 'owner__last_name']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
