from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer, EventListSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Event instances.
    """
    queryset = Event.objects.select_related('animal', 'animal__owner').all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['event_type', 'animal', 'date']
    search_fields = ['title', 'description', 'animal__tag_id', 'veterinarian']
    ordering_fields = ['date', 'time', 'cost']
    ordering = ['-date', '-time']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventSerializer
