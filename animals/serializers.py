from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    owner_name = serializers.CharField(source='owner.full_name', read_only=True)
    age_months = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class AnimalListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    owner_name = serializers.CharField(source='owner.full_name', read_only=True)
    age_months = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Animal
        fields = ['id', 'tag_id', 'name', 'species', 'breed', 'gender', 
                  'date_of_birth', 'age_months', 'weight', 'status', 
                  'owner', 'owner_name', 'image']
