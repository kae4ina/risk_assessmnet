from django.db import models
from django.db.models import ForeignKey, CASCADE

from assets.models import DefaultAssetCategory


class DefaultVulnerability(models.Model):
    name = models.CharField(max_length=150)
    related_asset_category = ForeignKey(to=DefaultAssetCategory, on_delete=CASCADE, default=1)

    def __self__(self):
        return self.name


class ThreatType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class DefaultThreat(models.Model):
    threat_name = models.CharField(max_length=150)
    threat_type = ForeignKey(to=ThreatType, on_delete=CASCADE)

    def __str__(self):
        return self.threat_name

class DefaultMeasure(models.Model):
    name=models.CharField(max_length=300)
    description = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.name


# Create your models here.
class RulesVuln(models.Model):
    vuln=ForeignKey(to=DefaultVulnerability, on_delete=CASCADE)
    measure=ForeignKey(to=DefaultMeasure, on_delete=CASCADE)

class RulesThreat(models.Model):
    threat=ForeignKey(to=DefaultThreat, on_delete=CASCADE)
    measure = ForeignKey(to=DefaultMeasure, on_delete=CASCADE)

