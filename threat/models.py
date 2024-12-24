from django.db import models

class DefaultThreat(models.Model):
    threat_name=models.CharField(max_length=150)

# Create your models here.
