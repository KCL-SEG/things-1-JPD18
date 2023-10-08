from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False, default='guy')
    description = models.TextField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],default =0 )