from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE

from company.models import Company
from threat.models import UserThreat


class Risk(models.Model):
    name=models.CharField(max_length=150)
    exploit_possibility=models.FloatField(
        validators=[
            MinValueValidator(0.0),  # Минимальное значение 0.0
            MaxValueValidator(100.0)  # Максимальное значение 100.0
        ]
    )
    related_threat=ForeignKey(to=UserThreat, on_delete=CASCADE)
    related_company=ForeignKey(to=Company, on_delete=CASCADE, default=4)
    def __str__(self):
        return self.name
# Create your models here.
