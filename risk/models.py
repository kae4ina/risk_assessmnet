from tkinter.constants import CASCADE

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey,CASCADE

from threat.models import UserThreat


# Create your models here.
class Risk(models.Model):
    name=models.CharField(max_length=150)
    exploit_possibility=models.FloatField(
        validators=[
        MinValueValidator(0.0),
        MaxValueValidator(100.0),
    ]
    )
    related_threat=ForeignKey(to=UserThreat, on_delete=CASCADE)
    def __str__(self):
        return self.name