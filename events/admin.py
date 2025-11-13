from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_type', 'animal', 'date', 'time', 'title', 'cost']
    list_filter = ['event_type', 'date']
    search_fields = ['title', 'description', 'animal__tag_id', 'veterinarian']
    date_hierarchy = 'date'
    readonly_fields = ['created_at', 'updated_at']
