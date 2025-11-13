from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ReportListSerializer(serializers.ModelSerializer):
    """Simplified serializer for list views"""
    class Meta:
        model = Report
        fields = ['id', 'title', 'report_type', 'start_date', 
                  'end_date', 'created_at']
