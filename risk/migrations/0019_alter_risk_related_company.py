# Generated by Django 5.1.1 on 2025-01-31 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_companyuser'),
        ('risk', '0018_risk_related_vulnerability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='related_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
