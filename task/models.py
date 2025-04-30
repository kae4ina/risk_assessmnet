from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils import timezone

from company.models import Company
from measure.models import UserMeasure
from solver.models import DefaultMeasure
from solver.models import UserRisk


class TaskStatus(models.Model):
    name=models.CharField(max_length=30)


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True, blank=True)

    default_measure = models.ForeignKey(
        to=DefaultMeasure,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks'
    )

    user_measure = models.ForeignKey(
        to=UserMeasure,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='tasks'
    )

    user_risk = models.ForeignKey(
        to='solver.UserRisk',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    status = models.ForeignKey(to=TaskStatus, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Task: {self.name}"

    @property
    def company(self):
        """Получаем компанию через связанный риск"""
        return self.user_risk.company

    @property
    def measure(self):
        return self.user_measure or self.default_measure

    def clean(self):
        if self.user_measure and self.default_measure:
            raise ValidationError("Задача может быть связана только с одной мерой (пользовательской или системной)")
        if not self.user_measure and not self.default_measure:
            raise ValidationError("Задача должна быть связана с мерой (пользовательской или системной)")