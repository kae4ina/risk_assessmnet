# Generated by Django 5.1.1 on 2025-03-18 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threat', '0015_defaultthreat_threat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultthreat',
            name='threat_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threat.threattype'),
        ),
    ]
