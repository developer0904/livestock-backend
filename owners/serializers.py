from rest_framework import serializers
from .models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    animal_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Owner
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class OwnerListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    full_name = serializers.CharField(read_only=True)
    animal_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email', 
                  'phone', 'farm_name', 'city', 'state', 'is_active', 'animal_count']
