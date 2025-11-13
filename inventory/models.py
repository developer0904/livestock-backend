from django.db import models
from django.core.validators import MinValueValidator


class InventoryItem(models.Model):
    """Model representing inventory items (feed, medicine, equipment, etc.)"""
    
    CATEGORY_CHOICES = [
        ('feed', 'Feed'),
        ('medicine', 'Medicine'),
        ('equipment', 'Equipment'),
        ('supplement', 'Supplement'),
        ('other', 'Other'),
    ]
    
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('lb', 'Pounds'),
        ('ltr', 'Liters'),
        ('gal', 'Gallons'),
        ('unit', 'Units'),
        ('bag', 'Bags'),
        ('bottle', 'Bottles'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    # Stock Information
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    reorder_level = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Pricing
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    # Supplier Information
    supplier_name = models.CharField(max_length=200, blank=True, null=True)
    supplier_contact = models.CharField(max_length=200, blank=True, null=True)
    
    # Dates
    last_purchased = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['name']),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
    
    @property
    def is_low_stock(self):
        """Check if stock is below reorder level"""
        return self.quantity <= self.reorder_level
    
    @property
    def total_value(self):
        """Calculate total value of stock"""
        return self.quantity * self.unit_price
