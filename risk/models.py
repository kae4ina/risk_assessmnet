from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CharField, ForeignKey, CASCADE

from company.models import Company
from threat.models import UserThreat
from vulnerability.models import UserVulnerability


class RiskDecision(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name


class Risk(models.Model):
    name=models.CharField(max_length=150)
    decision=ForeignKey(to=RiskDecision, null=True,on_delete=CASCADE)
    related_threat=ForeignKey(to=UserThreat, on_delete=CASCADE)
    related_vulnerability=ForeignKey(to=UserVulnerability,on_delete=CASCADE, default=12)
    related_company=ForeignKey(to=Company, on_delete=CASCADE)
    def __str__(self):
        return self.name


















    @property
    def risk_probability(self):
        # Получаем значения вероятностей
        exploit_possibility = self.related_vulnerability.exploit_possibility
        possibility = self.related_threat.possibility
        # Вычисляем среднее арифметическое
        return (exploit_possibility + possibility) / 2
# Create your models here.
