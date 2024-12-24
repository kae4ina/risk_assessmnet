from django.db import models
from django.db.models import ForeignKey, CASCADE
from django.forms import CharField


class DefaultCompanyArea(models.Model):
    default_company_area = models.CharField(max_length=100)
    def __str__(self):
        return self.default_company_area


class Company(models.Model):
    default_company_area = ForeignKey(to=DefaultCompanyArea, on_delete=CASCADE)
    company_name=models.CharField(max_length=200)
    def __str__(self):
        return self.company_name
# Create your models here.
