from django.db import models
from django.core.validators import MinValueValidator


class Animal(models.Model):
    """Model representing a livestock animal"""
    
    SPECIES_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('pig', 'Pig'),
        ('poultry', 'Poultry'),
        ('other', 'Other'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('sick', 'Sick'),
        ('pregnant', 'Pregnant'),
        ('sold', 'Sold'),
        ('deceased', 'Deceased'),
    ]
    
    # Basic Information
    tag_id = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    color = models.CharField(max_length=50, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='animals/', blank=True, null=True)
    
    # Ownership
    owner = models.ForeignKey('owners.Owner', on_delete=models.CASCADE, related_name='animals')
    acquisition_date = models.DateField()
    acquisition_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Health & Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='healthy')
    last_checkup = models.DateField(blank=True, null=True)
    health_notes = models.TextField(blank=True, null=True)
    
    # Breeding Information
    mother_tag = models.CharField(max_length=50, blank=True, null=True)
    father_tag = models.CharField(max_length=50, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['tag_id']),
            models.Index(fields=['species']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"{self.tag_id} - {self.name or self.breed}"
    
    @property
    def age_months(self):
        """Calculate age in months"""
        from datetime import date
        today = date.today()
        return (today.year - self.date_of_birth.year) * 12 + (today.month - self.date_of_birth.month)
