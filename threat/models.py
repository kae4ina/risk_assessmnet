from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey, CASCADE

from assets.models import Asset


class DefaultThreat(models.Model):
    threat_name=models.CharField(max_length=150)

class UserThreat(models.Model):
    name=models.CharField(max_length=150)
    possibility=models.FloatField(
        validators=[
            MinValueValidator(0.0),  # Минимальное значение 0.0
            MaxValueValidator(100.0)  # Максимальное значение 100.0
        ]
    )
    related_asset=ForeignKey(to=Asset, on_delete=CASCADE, default=1)
    def __str__(self):
        return self.name

# Create your models here.
