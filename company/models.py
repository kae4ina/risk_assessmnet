from django.contrib.auth.models import User
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

class CompanyUser(models.Model):
    company=models.ForeignKey(Company, on_delete=CASCADE)
    user=models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
      # return f"{self.user.username}-{self.company.company_name}"
      return f"{self.company.company_name}" #иначе отображается и полльзователь и компания
