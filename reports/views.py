from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Report
from .serializers import ReportSerializer, ReportListSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Report instances.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['report_type', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ReportListSerializer
        return ReportSerializer
