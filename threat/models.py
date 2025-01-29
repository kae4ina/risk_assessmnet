from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey, CASCADE

from assets.models import Asset
from company.models import Company


class DefaultThreat(models.Model):
    threat_name=models.CharField(max_length=150)

class UserThreat(models.Model):
    name=models.CharField(max_length=150)
    possibility=models.FloatField(
        default=50.00,
        validators=[
            MinValueValidator(0.0),  # Минимальное значение 0.0
            MaxValueValidator(100.0)  # Максимальное значение 100.0
        ]
    )
    related_asset=ForeignKey(to=Asset, on_delete=CASCADE)
    def __str__(self):
        return self.name

class CompanyThreat(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    threat = models.ForeignKey(UserThreat, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.company} - {self.threat}"

    class Meta:
        unique_together = ('company', 'threat')

# Create your models here.
