from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal
from .serializers import AnimalSerializer, AnimalListSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Animal instances.
    """
    queryset = Animal.objects.select_related('owner').all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['species', 'breed', 'gender', 'status', 'owner']
    search_fields = ['tag_id', 'name', 'breed', 'owner__first_name', 'owner__last_name']
    ordering_fields = ['tag_id', 'date_of_birth', 'weight', 'acquisition_date']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalListSerializer
        return AnimalSerializer
