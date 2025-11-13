from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem
from .serializers import InventoryItemSerializer, InventoryItemListSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing InventoryItem instances.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'unit']
    search_fields = ['name', 'sku', 'supplier_name']
    ordering_fields = ['name', 'quantity', 'unit_price', 'last_purchased']
    ordering = ['name']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return InventoryItemListSerializer
        return InventoryItemSerializer
