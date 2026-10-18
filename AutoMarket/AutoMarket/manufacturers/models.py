from django.db import models

from common.models import TimeStampedModel
from common.validators import FoundedYearValidator

class Manufacturer(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100, null=False, blank=False)
    founded_year = models.IntegerField(null=False, blank=False, validators=[FoundedYearValidator("Year must be between 1800 and current year")])
    logo_url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name