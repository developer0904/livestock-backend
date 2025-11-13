from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Owner
from .serializers import OwnerSerializer, OwnerListSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Owner instances.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'city', 'state']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'farm_name']
    ordering_fields = ['last_name', 'first_name', 'created_at']
    ordering = ['last_name', 'first_name']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return OwnerListSerializer
        return OwnerSerializer
