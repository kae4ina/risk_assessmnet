from django.db import models
from django.db.models import ForeignKey, CASCADE

from assets.models import DefaultAssetCategory


class DefaultVulnerability(models.Model):
    name = models.CharField(max_length=150)

    def __self__(self):
        return self.name


class ThreatType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class DefaultThreat(models.Model):
    id = models.CharField(max_length=150, primary_key=True)

    name = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    source = models.CharField(max_length=500, null=True)
    destination = models.CharField(max_length=500, null=True)

    destruction_of_confidence = models.BooleanField(null=True)
    destruction_of_integrity = models.BooleanField(null=True)
    destruction_of_availability = models.BooleanField(null=True)
    def __str__(self):
        return self.name

class DefaultMeasureGroup(models.Model):
    id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class DefaultMeasureSubgroup(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    group = ForeignKey(to=DefaultMeasureGroup, on_delete=CASCADE, default=1, null=True)
    name = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

class DefaultMeasure(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=500)
    subgroup = ForeignKey(to=DefaultMeasureSubgroup, on_delete=CASCADE, default=1)
    #related_threat = ForeignKey(to=DefaultThreat, on_delete=CASCADE, default=1)  # парируемая угроза
    def __str__(self):
        return self.name


class RulesVuln(models.Model):
    vuln=ForeignKey(to=DefaultVulnerability, on_delete=CASCADE)
    measure=ForeignKey(to=DefaultMeasure, on_delete=CASCADE)

class RulesThreat(models.Model):
    measure = ForeignKey(to=DefaultMeasure, on_delete=CASCADE)
    threat=ForeignKey(to=DefaultThreat, on_delete=CASCADE, default=1)
    def __str__(self):
        measure_name = self.measure.name if hasattr(self.measure, 'name') else "Мера не указана"
        threat_name = self.threat.name if hasattr(self.threat, 'name') else "Угроза не указана"

        return f"Правило: Мера — {measure_name}, Угроза — {threat_name}"


