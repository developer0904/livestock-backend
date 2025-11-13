from rest_framework import serializers
from .models import InventoryItem


class InventoryItemSerializer(serializers.ModelSerializer):
    is_low_stock = serializers.BooleanField(read_only=True)
    total_value = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class InventoryItemListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    is_low_stock = serializers.BooleanField(read_only=True)
    total_value = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'category', 'quantity', 'unit', 
                  'reorder_level', 'unit_price', 'total_value', 'is_low_stock']
