from django.db import models
from django.db.models import ForeignKey, CASCADE

from assets.models import Asset


class DefaultThreat(models.Model):
    threat_name=models.CharField(max_length=150)

class UserThreat(models.Model):
    name=models.CharField(max_length=150)
    related_assets = models.ManyToManyField(Asset)
    def __str__(self):
        return self.name
# Create your models here.
