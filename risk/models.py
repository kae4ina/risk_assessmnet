from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE

from threat.models import UserThreat


class Risk(models.Model):
    name=models.CharField(max_length=150)
    exploit_possability=models.FloatField(
        validators=[
            MinValueValidator(0.0),  # Минимальное значение 0.0
            MaxValueValidator(100.0)  # Максимальное значение 100.0
        ]
    )
    related_threat=ForeignKey(to=UserThreat, on_delete=CASCADE)
    def __str__(self):
        return self.name
# Create your models here.
