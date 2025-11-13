from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    animal_tag = serializers.CharField(source='animal.tag_id', read_only=True)
    animal_name = serializers.CharField(source='animal.name', read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class EventListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    animal_tag = serializers.CharField(source='animal.tag_id', read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'event_type', 'animal', 'animal_tag', 'date', 
                  'time', 'title', 'cost', 'veterinarian']
