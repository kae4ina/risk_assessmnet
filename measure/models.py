from django.db import models
from django.db.models import ForeignKey, CASCADE

from company.models import Company
from risk.models import Risk
from solver.models import UserRisk


class DefaultMeasure(models.Model):
    name=models.CharField(max_length=150)
# Create your models here.
class UserMeasure(models.Model):
    name=models.CharField(max_length=150)
    description=models.CharField(max_length=1000, null=True, blank=True)
    related_risk=ForeignKey(to=UserRisk,on_delete=CASCADE, default=6)
    related_company=ForeignKey(to=Company, on_delete=CASCADE)

    def __str(self):
        return self.name