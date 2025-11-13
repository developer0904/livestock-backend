from django.db import models
from django.core.validators import MinValueValidator


class Event(models.Model):
    """Model representing events related to livestock (births, deaths, treatments, etc.)"""
    
    EVENT_TYPE_CHOICES = [
        ('birth', 'Birth'),
        ('death', 'Death'),
        ('sale', 'Sale'),
        ('purchase', 'Purchase'),
        ('vaccination', 'Vaccination'),
        ('treatment', 'Treatment'),
        ('checkup', 'Health Checkup'),
        ('breeding', 'Breeding'),
        ('weaning', 'Weaning'),
        ('other', 'Other'),
    ]
    
    # Event Details
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    animal = models.ForeignKey('animals.Animal', on_delete=models.CASCADE, related_name='events')
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    
    # Event Specific Information
    title = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    
    # Additional Information
    veterinarian = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    # Documents
    attachments = models.FileField(upload_to='events/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-time']
        indexes = [
            models.Index(fields=['event_type']),
            models.Index(fields=['date']),
            models.Index(fields=['animal']),
        ]
    
    def __str__(self):
        return f"{self.event_type} - {self.animal.tag_id} - {self.date}"
