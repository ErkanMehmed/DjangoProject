from django.utils import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from common.models import TimeStampedModel

from manufacturers.models import Manufacturer

def current_year():
    return timezone.now().year

class Feature(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Vehicle(TimeStampedModel):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='vehicles')
    model_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1886), MaxValueValidator(current_year)])
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    mileage = models.PositiveIntegerField(default=0)
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    color = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    features = models.ManyToManyField(Feature, blank=True, related_name='vehicles')
    horsepower = models.PositiveSmallIntegerField(null=True, blank=True)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='used')
    doors = models.PositiveSmallIntegerField(default=4, validators=[MinValueValidator(2), MaxValueValidator(6)])

    def __str__(self):
        return f'{self.manufacturer} {self.model_name} ({self.year})'