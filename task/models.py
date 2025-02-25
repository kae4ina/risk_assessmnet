from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.utils import timezone

from company.models import Company
from measure.models import UserMeasure

class TaskStatus(models.Model):
    name=models.CharField(max_length=30)


class Task (models.Model):
    name=models.CharField(max_length=150)
    description = models.CharField(max_length=1000, null=True, blank=True)
    related_measure=ForeignKey(to=UserMeasure ,on_delete=CASCADE)
    related_company = ForeignKey(to=Company, on_delete=CASCADE)

    status=ForeignKey(to=TaskStatus, on_delete=CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)  # Дата и время начала задачи
    end_date = models.DateTimeField(null=True, blank=True)  # Дата и время окончания задачи

    def __str__(self):
        return f"Task: {self.name}"



