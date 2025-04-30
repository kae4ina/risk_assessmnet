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
        # Получаем все связанные угрозы и уязвимости
        threats = self.risk_threats.all()  # связанные угрозы
        vulnerabilities = self.risk_vulnerabilities.all()  # связанные уязвимости

        # Суммируем значения вероятностей
        total_exploit_possibility = sum(vulnerability.exploit_possibility for vulnerability in vulnerabilities)
        total_possibility = sum(threat.possibility for threat in threats)

        # Общее количество угроз и уязвимостей
        total_count = len(threats) + len(vulnerabilities)

        # Если нет связанных угроз и уязвимостей, возвращаем 0
        if total_count == 0:
            return 0

        # Вычисляем среднюю вероятность
        average_probability = (total_exploit_possibility + total_possibility) / total_count
        return average_probability


class RiskThreat(models.Model):
        risk = models.ForeignKey(Risk, related_name='risk_threats', on_delete=models.CASCADE)
        threat = models.ForeignKey(UserThreat, on_delete=models.CASCADE)

class RiskVulnerability(models.Model):
        risk = models.ForeignKey(Risk, related_name='risk_vulnerabilities', on_delete=models.CASCADE)
        vulnerability = models.ForeignKey(UserVulnerability, on_delete=models.CASCADE)


# Create your models here.
