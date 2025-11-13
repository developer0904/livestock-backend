from django.db import models


class Report(models.Model):
    """Model representing generated reports"""
    
    REPORT_TYPE_CHOICES = [
        ('inventory', 'Inventory Report'),
        ('health', 'Health Report'),
        ('financial', 'Financial Report'),
        ('breeding', 'Breeding Report'),
        ('custom', 'Custom Report'),
    ]
    
    # Report Information
    title = models.CharField(max_length=200)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    
    # Report Data (stored as JSON)
    data = models.JSONField()
    
    # Date Range
    start_date = models.DateField()
    end_date = models.DateField()
    
    # File
    file = models.FileField(upload_to='reports/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['report_type']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"{self.title} - {self.created_at.date()}"
